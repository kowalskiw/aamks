#!/usr/bin/python3

import os
import shutil
import sys


from evac.evacuee import Evacuee
from evac.evacuees import Evacuees
from evac.rvo2_dto import EvacEnv
from fire.smoke_query import SmokeQuery
from include import Sqlite
import time
import logging
from urllib.request import urlopen, urlretrieve
from include import Json
import json
from collections import OrderedDict
from subprocess import Popen
import zipfile
from include import SendMessage


#SIMULATION_TYPE = 'NO_CFAST'
SIMULATION_TYPE = 1
SendMessage("Start simulations")




class Worker:

    def __init__(self):
        self.url = sys.argv[1]
        self.vars = OrderedDict()
        self.results = dict()
        self.obstacles = None
        self.trajectory = None
        self.velocity = None
        self.floor_dims = None
        self.evacuees = None
        self.fire_dto = None
        self.sim_floors = None
        self.start_time = time.time()
        self.floors = list()
        os.chdir('/home/aamks')

    def _report_error(self, exception: Exception) -> logging:
        print('Error occurred, see aamks.log file for details.')
        logging.error('Cannot create RVO2 environment: {}'.format(str(exception)))
        sys.exit(1)

    def get_config(self):
        try:
            f = open('{}/{}/config.json'.format(os.environ['AAMKS_PATH'], 'evac'), 'r')
            self.config = json.load(f)
        except Exception as e:
            print('Cannot read config file: {}'.format(e))
            sys.exit(1)

        try:
            self.vars['conf'] = json.loads(urlopen('{}/evac.json'.format(self.url)).read().decode())
        except Exception as e:
            print('Cannot fetch evac.json from server: {}'.format(str(e)))
            sys.exit(1)
        else:
            print('URL OK. Starting calculations')

        self.sim_id = self.vars['conf']['SIM_ID']
        self.host_name = os.uname()[1]
        self.db_server = self.vars['conf']['SERVER']

    def get_geom_and_cfast(self):

        os.chdir(self.vars['conf']['WORKSPACE'])

        logging.basicConfig(filename='aamks.log', level=logging.INFO,
                            format='%(asctime)s %(levelname)s: %(message)s')

        logging.info('URL: {}'.format(self.url))

        try:
            urlretrieve('{}/../../aamks.sqlite'.format(self.url), 'aamks.sqlite')

        except Exception as e:
            self._report_error(e)
        else:
            logging.info('Aamks.sqlite fetched from server')

        try:
            self.cfast_input = urlopen('{}/cfast.in'.format(self.url)).read().decode()

        except Exception as e:
            self._report_error(e)
        else:
            logging.info('Cfast.in fetched from server')
        print("Host: {} start simulation id: {}".format(self.host_name, self.sim_id))

    def _create_workspace(self):
        try:
            shutil.rmtree(self.vars['conf']['WORKSPACE'], ignore_errors=True)
            os.makedirs(self.vars['conf']['WORKSPACE'])
        except Exception as e:
            self._report_error(e)

    def run_cfast_simulations(self):

        try:
            with open('cfast.in', "w") as f:
                f.write(self.cfast_input)
        except Exception as e:
            self._report_error(e)
        else:
            logging.debug('Cfast input file saved.')

        try:
            os.system('/usr/local/aamks/fire/cfast cfast.in')
            cfast_log = open('cfast.log', 'r')
        except Exception as e:
            self._report_error(e)

        for line in cfast_log.readlines():
            if line.startswith("***Error:"):
                self._report_error(Exception(line))

        logging.info('Simulation finished with exit code 0')

    def create_geom_database(self):

        self.s = Sqlite("aamks.sqlite")
        #self.s.dumpall()
        self.obstacles = json.loads(self.s.query('SELECT * FROM obstacles')[0]['json'], object_pairs_hook=OrderedDict)

    def _create_evacuees(self, floor):

        evacuees = []
        logging.debug('Adding evacuues on floor: {}'.format(floor))

        floor = self.vars['conf']['FLOORS_DATA'][str(floor)]

        for i in range(floor['NUM_OF_EVACUEES']):
            evacuees.append(Evacuee(origin=tuple(floor['EVACUEES']['E' + str(i)]['ORIGIN']),
                                    v_speed=floor['EVACUEES']['E' + str(i)]['V_SPEED'],
                                    h_speed=floor['EVACUEES']['E' + str(i)]['H_SPEED'],
                                    roadmap=floor['EVACUEES']['E' + str(i)]['ROADMAP'],
                                    pre_evacuation=floor['EVACUEES']['E' + str(i)][
                                        'PRE_EVACUATION'],
                                    alpha_v=floor['EVACUEES']['E' + str(i)]['ALPHA_V'],
                                    beta_v=floor['EVACUEES']['E' + str(i)]['BETA_V'],
                                    node_radius=self.config['NODE_RADIUS']))

        e = Evacuees()
        [e.add_pedestrian(i) for i in evacuees]

        logging.info('Num of evacuees placed: {}'.format(len(evacuees)))
        return e

    def prepare_simulations(self):
        logging.info('Number of floors processed: {}'.format(len(self.obstacles['points'])))
        obstacles = []

        for i in range(len(self.obstacles['points'])):
            try:
                env = EvacEnv(self.vars['conf'])
                env.floor = i
            except Exception as e:
                self._report_error(e)
            else:
                logging.info('RVO2 ready on {} floors'.format(i))

            for obst in self.obstacles['points'][str(i)]:
                obstacles.append([tuple(x) for x in obst])
            env.obstacle = obstacles
            num_of_vertices = env.process_obstacle(obstacles)
            logging.info('Added obstacles on floor: {}, number of vercites: {}'.format(str(i+1), num_of_vertices))

            e = self._create_evacuees(i)
            env.place_evacuees(e)
            self.floors.append(env)

    def do_simulation(self):
        logging.info('Starting simulaitons')

        time_frame = 10
        floor = 0
        try:
            master_query = SmokeQuery(floor='0', vars=self.config)
        except Exception as e:
            self._report_error(e)

        for i in self.floors:
            try:
                i.smoke_query = SmokeQuery(floor=str(floor), vars=self.config)
            except Exception as e:
                self._report_error(e)
            else:
                logging.info('Smoke query connected to floor: {}'.format(floor))
            floor += 1
        while 1:
            if master_query.cfast_has_time(time_frame) == 1:
                logging.info('Simulation time: {}'.format(time_frame))
                for i in self.floors:
                    i.read_cfast_record(time_frame)
                    i.do_simulation(time_frame)
                time_frame += 10
            else:
                time.sleep(1)
            if time_frame > 80:
                break


    def send_report(self, sim_id, project,floor, animation_data, psql_data ): # {{{
        '''
        Runs on a worker. Write /home/aamks/project/sim_id.json on each aRun
        completion. Then inform gearman server to scp to itself
        /home/aamks/project/sim_id.json via aOut service. Gearman server will
        process this json via /usr/local/aamks/manager/results_collector.py.
        Gearman server will psql insert and will scp the worker's animation to
        itself.
        '''

        self.project_dir="/home/aamks/{}".format(project)
        try:
            os.makedirs(self.project_dir, exist_ok=True)
        except:
            pass
        self.sim_id=sim_id
        self.floor=floor
        self._write_animation(animation_data)
        self._write_report(psql_data)
    # }}}
    def _write_animation(self):# {{{
        '''
        Raw data comes as an argument. We create /home/aamks/1.anim.zip
        with anim.json inside.
        '''

        floor = 0
        for i in self.floors:
            animation_data = i.record_data()
            zf = zipfile.ZipFile("f{}_s{}.anim.zip".format(floor, self.sim_id), mode='w',
                                 compression=zipfile.ZIP_DEFLATED)
            try:
                zf.writestr("anim.json", json.dumps(animation_data))
            finally:
                zf.close()
            floor += 1

    # }}}
    def _write_report(self, psql_data):# {{{
        for num_floor in range(len(self.floors)):
            j=Json()
            host = os.uname()[1]
            report = OrderedDict()
            report['worker'] = host
            report['sim_id'] = self.sim_id
            report['animation'] = "{}_{}.anim.zip".format(num_floor, self.sim_id)
            report['psql']=psql_data
            json_file = "report{}_{}.json".format(num_floor, self.sim_id)
            j.write(report, json_file)
            Popen("gearman -h {} -f aOut '{} {} {} {}'".format(os.environ['AAMKS_SERVER'],
                                                           host, json_file, self.sim_id, num_floor), shell=True)
    # }}}


    def _write_animation_file(self, anim_json, floor):# {{{

        self.jsonOut = OrderedDict()
        self.jsonOut['sort_id'] = int(self.sim_id)
        self.jsonOut['title'] = "sim{}, f{}".format(self.sim_id, floor)
        self.jsonOut['floor'] = floor
        self.jsonOut['fire_origin'] = self.vars['conf']['ROOM_OF_FIRE_ORIGIN']
        self.jsonOut['highlight_geom'] = None
        self.jsonOut['anim']="{}/f{}_s{}.anim.zip".format(self.sim_id, floor, self.sim_id)

        anim_json.append(self.jsonOut)

        return anim_json

    # }}}

    def _copy_animation_files(self):

        json = Json()
        anim_json = json.read('{}/workers/vis/anims.json'.format(os.environ['AAMKS_PROJECT']))

        for i in self.vars['conf']['FLOORS_DATA'].keys():
            shutil.copy('f{}_s{}.anim.zip'.format(i, self.sim_id), '{}/{}/{}'.format(os.environ['AAMKS_PROJECT'], 'workers', self.sim_id))
            anim_json = self._write_animation_file(anim_json, i)

        json.write(anim_json, '{}/workers/vis/anims.json'.format(os.environ['AAMKS_PROJECT']))


    def main(self):
        self.get_config()
        self._create_workspace()
        self.get_geom_and_cfast()
        self.create_geom_database()
        self.run_cfast_simulations()
        self.prepare_simulations()
        self.do_simulation()
        self._write_animation()
        self._write_report('psql_connect')
        self._copy_animation_files()

    def test(self):
        self.get_config()
        self.get_geom_and_cfast()
        self.create_geom_database()
        self.prepare_simulations()
        self.do_simulation()
        self._write_animation()
        self._write_report('psql_connect')
        self._copy_animation_files()


try:
    w = Worker()
except Exception as e:
    SendMessage(e)
else:
    SendMessage("Alles in grunem bereisch")

if SIMULATION_TYPE == 'NO_CFAST':
    try:
        w.test()
    except Exception as e:
        SendMessage(e)
    else:
        SendMessage("Alles in grunem bereisch")
else:
    try:
        w.main()
    except Exception as e:
        SendMessage(e)
    else:
        SendMessage("Alles in grunem bereisch")
