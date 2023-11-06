import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http'


@Component({
  selector: 'app-controls',
  templateUrl: './controls.component.html',
  styleUrls: ['./controls.component.css']
})
export class ControlsComponent {
  albums: any[] = []

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http.get<any[]>('/assets/albums.json').subscribe((albums) => {
      this.albums = albums
      console.log(this.albums)
    })
  }

}
