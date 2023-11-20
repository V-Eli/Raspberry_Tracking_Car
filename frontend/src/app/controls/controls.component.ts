import { Component, OnInit, ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { JoystickEvent, NgxJoystickComponent } from 'ngx-joystick';
import { JoystickManagerOptions, JoystickOutputData } from 'nipplejs';
import { MatSlideToggleChange } from '@angular/material/slide-toggle';



@Component({
  selector: 'app-controls',
  templateUrl: './controls.component.html',
  styleUrls: ['./controls.component.css']
})
export class ControlsComponent implements OnInit {
  public forward = 'http://127.0.0.1:8000/car_forward';
  public stop = 'http://127.0.0.1:8000/car_stop';
  public backward = 'http://127.0.0.1:8000/backward';
  public url4 = 'https://example.com/endpoint2';
  private socket: WebSocket | undefined;
  private socket2: WebSocket | undefined;

  title = 'ngx-joystick-demo';
  @ViewChild('staticJoystic') staticJoystick!: NgxJoystickComponent;

  staticOptions: JoystickManagerOptions = {
    mode: 'static',
    position: { left: '50%', top: '50%' },
    color: 'blue',
  };

  staticOutputData!: JoystickOutputData;

  directionStatic!: string;
  interactingStatic!: boolean;

  albums: any[] = []

  constructor(private http: HttpClient) {
    this.socket = undefined;
    this.socket2 = undefined;
    
  }

  private sendJoystickData(degree: number, socket: WebSocket) {
    // Convert the degree to a JSON string
    const jsonData = JSON.stringify({ degree });
  
    // Send the JSON string to the WebSocket server
    socket.send(jsonData);
  }

  public videoSource: string | undefined;

  

  ngOnInit() {
    // Connect to a WebSocket server
    this.socket = new WebSocket('wss://example.com/socket');
    this.socket2 = new WebSocket('wss://example2.com/socket2');

     // Handle messages received from the video WebSocket
     this.socket2.addEventListener('message', (event) => {
      // Assuming the data is a base64 encoded video stream
      this.videoSource = 'data:video/mp4;base64,' + event.data;
    });

  }

  //Post when the buttons are touched
  sendPostRequest(url: string) {
    // You can add any request data or headers as needed
    const requestData = { key: 'value' };
  
    this.http.post(url, requestData)
      .subscribe({
        next: (response) => {
          // Handle the successful response here
          console.log('POST request was successful', response);
        },
        error: (error) => {
          // Handle any errors that occur during the request
          console.error('Error sending POST request', error);
        }
      });
  }

  // Fuction that checks for the joystick movement
  onMoveStatic(event: JoystickEvent) {
    this.staticOutputData = event.data;

    // Check if the WebSocket connection is open
    if (this.socket && this.socket.readyState === WebSocket.OPEN) {
      // Send joystick data to the WebSocket server
      this.sendJoystickData(this.staticOutputData.angle.degree, this.socket);
    }
  }

  // Function to send the state of the toggle with the sendPostRequest
  onToggleChange(event: MatSlideToggleChange) {
    if (event.checked) {
      // Send a POST request when the toggle is turned on
      this.sendPostRequest('https://example.com/on');
    } else {
      // Send a different POST request when the toggle is turned off
      this.sendPostRequest('https://example.com/off');
    }
  }


}
