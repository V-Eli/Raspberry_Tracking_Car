import { Component, OnInit, ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { JoystickEvent, NgxJoystickComponent } from 'ngx-joystick';
import { JoystickManagerOptions, JoystickOutputData } from 'nipplejs';
import { webSocket } from 'rxjs/webSocket';
import { MatSlideToggleChange } from '@angular/material/slide-toggle';



@Component({
  selector: 'app-controls',
  templateUrl: './controls.component.html',
  styleUrls: ['./controls.component.css']
})
export class ControlsComponent implements OnInit {
  public url1 = 'https://example.com/endpoint1';
  public url2 = 'https://example.com/endpoint2';
  public url3 = 'https://example.com/endpoint1';
  public url4 = 'https://example.com/endpoint2';
  private socket: WebSocket | undefined;
  private socket2: WebSocket | undefined;

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

  constructor(private http: HttpClient) {
    this.socket = undefined;
    this.socket2 = undefined;
    
  }

  ngOnInit() {
    this.http.get<any[]>('/assets/albums.json').subscribe((albums) => {
      this.albums = albums
      console.log(this.albums)
    })

    // Connect to a WebSocket server
    this.socket = new WebSocket('wss://example.com/socket');
    this.socket2 = new WebSocket('wss://example2.com/socket2');

    // Listen for messages
    this.socket.addEventListener('message', (event) => {
      // Handle incoming WebSocket messages
      console.log('Received a message:', event.data);
    });

    // Handle WebSocket errors
    this.socket.addEventListener('error', (event) => {
      console.error('WebSocket error:', event);
    });
    
    // Handle WebSocket close event
    this.socket.addEventListener('close', (event) => {
      console.log('WebSocket connection closed:', event);
    });

    // Send messages
    this.socket.send('Hello, WebSocket!');
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

  onToggleChange(event: MatSlideToggleChange) {
    if (event.checked) {
      // Send a POST request when the toggle is turned on
      this.sendPostRequest('https://example.com/on');
    } else {
      // Send a different POST request when the toggle is turned off
      this.sendPostRequest('https://example.com/off');
    }
  }

  sendPostRequest(url: string) {
    // You can add any request data or headers as needed
    const requestData = { key: 'value' };
  
    this.http.post(url, requestData)
      .subscribe(
        (response) => {
          // Handle the successful response here
          console.log('POST request was successful', response);
        },
        (error) => {
          // Handle any errors that occur during the request
          console.error('Error sending POST request', error);
        }
      );
  }

}
