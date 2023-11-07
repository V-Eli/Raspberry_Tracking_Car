import { Component, OnInit, ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { JoystickEvent, NgxJoystickComponent } from 'ngx-joystick';
import { JoystickManagerOptions, JoystickOutputData } from 'nipplejs';


@Component({
  selector: 'app-controls',
  templateUrl: './controls.component.html',
  styleUrls: ['./controls.component.css']
})
export class ControlsComponent implements OnInit {
  title = 'ngx-joystick-demo';
  @ViewChild('staticJoystic') staticJoystick!: NgxJoystickComponent;
  @ViewChild('dynamicJoystick') dynamicJoystick!: NgxJoystickComponent;
  @ViewChild('semiJoystick') semiJoystick!: NgxJoystickComponent;

  staticOptions: JoystickManagerOptions = {
    mode: 'static',
    position: { left: '50%', top: '50%' },
    color: 'blue',
  };

  dynamicOptions: JoystickManagerOptions = {
    mode: 'dynamic',
    color: 'red',
    multitouch: true
  };

  semiOptions: JoystickManagerOptions = {
    mode: 'semi',
    catchDistance: 50,
    color: 'purple'
  };

  staticOutputData!: JoystickOutputData;
  semiOutputData!: JoystickOutputData;
  dynamicOutputData!: JoystickOutputData;

  directionStatic!: string;
  interactingStatic!: boolean;

  albums: any[] = []

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http.get<any[]>('/assets/albums.json').subscribe((albums) => {
      this.albums = albums
      console.log(this.albums)
    })
  }

  onStartStatic(event: JoystickEvent) {
    this.interactingStatic = true;
  }

  onEndStatic(event: JoystickEvent) {
    this.interactingStatic = false;
  }

  onMoveStatic(event: JoystickEvent) {
    this.staticOutputData = event.data;
  }

  onPlainUpStatic(event: JoystickEvent) {
    this.directionStatic = 'UP';
  }

  onPlainDownStatic(event: JoystickEvent) {
    this.directionStatic = 'DOWN';
  }

  onPlainLeftStatic(event: JoystickEvent) {
    this.directionStatic = 'LEFT';
  }

  onPlainRightStatic(event: JoystickEvent) {
    this.directionStatic = 'RIGHT';
  }

  onMoveSemi(event: JoystickEvent) {
    this.semiOutputData = event.data;
  }

  onMoveDynamic(event: JoystickEvent) {
    this.dynamicOutputData = event.data;
  }

}
