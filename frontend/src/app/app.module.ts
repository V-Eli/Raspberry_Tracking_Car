import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ControlsComponent } from './controls/controls.component';
import { HttpClientModule } from '@angular/common/http';
import { MatIconModule } from '@angular/material/icon';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatButtonModule } from '@angular/material/button';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgxJoystickModule } from 'ngx-joystick';


@NgModule({
  declarations: [
    AppComponent,
    ControlsComponent
  ],
  imports: [
    AppRoutingModule,
    BrowserModule,
    HttpClientModule,
    MatIconModule,
    MatSlideToggleModule,
    MatButtonModule,
    BrowserAnimationsModule,
    NgxJoystickModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
