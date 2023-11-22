# Installation

## Install Angular-Cli    
```bash
npm install -g @angular/cli
```    
## Create angular project
```bash
ng new frontend
```   
## Test the installation
```bash
ng serve
```    
## Add Material Icons to project
```bash
ng add @angular/material 
```
## Import the MatIconModule from @angular/material
Import the MatIconModule from @angular/material in your app.module.ts file    
```typescript
import {MatIconModule} from '@angular/material/icon';
```
## Include the MatIconModule in Your App Module Imports 
```typescript
@NgModule({
  imports: [ 
    ... 
    MatIconModule 
  ], 
  ... 
}) 
export class AppModule {}
```


# Create components

## Add controls component
```bash
ng g c controls
```

# Run the project

## Build the image
```bash
docker build -f frontend/Dockerfile -t tracking_frontend .
```

## Run the container
```bash
docker run -it --name tracking_frontend -p 4200:4200 tracking_frontend
```