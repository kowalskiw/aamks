import { Component, OnInit } from '@angular/core';
import { Main } from '../../../../../services/main/main';
import { MainService } from '../../../../../services/main/main.service';

@Component({
  selector: 'app-distributions',
  templateUrl: './distributions.component.html',
  styleUrls: ['./distributions.component.scss']
})
export class DistributionsComponent implements OnInit {

  main: Main;

  path: string;

  wcbe: string;
  dcbe: string;

  constructor(private mainService: MainService) { }

  ngOnInit() {
    this.mainService.getMain().subscribe(main => this.main = main);

    this.path = this.main.hostAddres + '/aamks_users/' + this.main.email + '/' + this.main.currentProject.id + '/risk/' + this.main.currentRiskScenario.id + '/picts/';

    this.wcbe = this.path + 'wcbe.png';
    this.dcbe = this.path + 'dcbe.png';
  }

}
