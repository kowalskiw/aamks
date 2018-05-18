import os 
import sys
import json
from subprocess import Popen,PIPE
from include import Json
from include import Sqlite
from include import SendMessage
from collections import OrderedDict
from include import Psql
import traceback

try:
    class ResultsCollector():
        def __init__(self, host, meta_file, sim_id):# {{{
            '''
            1. aamksrun makes gearman pass these jobs to workers: 
                /usr/local/aamks/tests/worker.py
            2. Worker calls gearman server aOut function
            3. This file implements gearman's aOut function:
                * download results.json with configuration to workers/123/report_123.json
                * download animation.zip to workers/123/anim.zip
            '''
            self.host=host
            self.meta_file=meta_file
            self.sim_id=sim_id
            self.meta = None

            self.json=Json()
            self._fetch_meta()
            self._animation()
# }}}
        def _fetch_meta(self):# {{{
            SendMessage("self.meta copied")
            try:
                Popen(["scp", "{}:{}".format(self.host, self.meta_file), self.meta_file]).wait()
            except Exception as e:
                SendMessage(e)
            else: 
                pass

            self.meta=self.json.read(self.meta_file)
# }}}
        def _fire_origin_coords(self, sim_id):# {{{
            room=self.meta['fire_origin']
            
            self.s=Sqlite("{}/aamks.sqlite".format(self.meta['path_to_project']))
            z=self.s.query("SELECT center_x, center_y FROM aamks_geom WHERE name=?", (room,))[0]
            return (z['center_x'], z['center_y'])
# }}}
        def _animation(self):# {{{
            source = self.host+':'+self.meta['path_to_project']+'workers/'+str(self.meta['sim_id'])+'/'+self.meta['animation']
            dest = self.meta['path_to_project']+'workers/'+str(self.meta['sim_id'])+'/'+self.meta['animation']
            Popen(["scp", source, dest])

            self.jsonOut=OrderedDict()
            self.jsonOut['sort_id']=int(sim_id)
            self.jsonOut['title']="sim{}, f{}".format(self.meta['sim_id'], self.meta['floor'])
            self.jsonOut['floor']=self.meta['floor']
            self.jsonOut['fire_origin']=self._fire_origin_coords(self.meta['sim_id'])
            self.jsonOut['highlight_geom']=None
            self.jsonOut['anim']="{}/{}".format(self.meta['sim_id'],self.meta['animation'])

            anims_master="{}/workers/vis/anims.json".format(self.meta['path_to_project'])
            try:
                z=self.json.read(anims_master)
            except:
                z=[]
            z.append(self.jsonOut)
            self.json.write(z, anims_master)
# }}}
        def psql_report(self):
            p = Psql()
            x = p.query('SELECT max(iteration)+1 FROM simulations WHERE project=%s', (self.meta['project_id'],))


    try:
        host=sys.argv[1]
        meta_file=sys.argv[2]
        sim_id=sys.argv[3]
    except:
        ''' Testing without gearman. Make sure workers/1/ exist and contains evac and cfast jsons. '''
        j=Json()
        c=j.read("{}/conf_aamks.json".format(os.environ['AAMKS_PROJECT']))
        host="localhost"
        meta_file="/home/aamks/{}/report_1.json".format(c['PROJECT_NAME'])
        sim_id="1"
        floor="1"

    ResultsCollector(host,meta_file,sim_id)

except:
    t="In results_collector.py:\n"
    t+=traceback.format_exc()
    SendMessage(t)
    raise Exception("worker fail")
