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
