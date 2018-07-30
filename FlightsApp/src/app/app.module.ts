// Modules
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { AppMaterialModule } from './app.module.material';
import { HttpModule } from '@angular/http';

//Services
import { AirportService } from './services/airport.service'
import { RouteService } from './services/route.service'

//Component
import { AppComponent } from './app.component';
import { NavTabsComponent } from './components/nav-tabs/nav-tabs.component';
import { FlightsSummaryComponent } from './components/flights-summary/flights-summary.component';
import { TableFlightsSummaryComponent } from './components/table-flights-summary/table-flights-summary.component';

@NgModule({
  declarations: [
    AppComponent,
    NavTabsComponent,
    FlightsSummaryComponent,
    TableFlightsSummaryComponent
  ],
  imports: [
    HttpModule,
    BrowserModule,
    BrowserAnimationsModule,
    AppMaterialModule
  ],
  providers: [
    AirportService,
    RouteService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }