import { Component, OnInit } from '@angular/core';
import { AirportService } from '../../services/airport.service';
import { TripService } from '../../services/trip.service';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import { MatTableDataSource } from '@angular/material';


export interface Airport {
  iata: string;
  city: string;
}

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {
  displayedColumns: string[] = ['departure_time', 'arrival_time', 'price', 'aircraft'];

  origin;
  destination;
  departure_date;
  airports: Airport[];
  trips;

  constructor(private airportService: AirportService, private tripService: TripService) { }

  ngOnInit() {
    this.getAllAirports();
  }

  getAllAirports(){
    this.airportService.getAllAirports().subscribe((res) => {
      this.airports = res;
    });
  }

  doSearch(){
    this.tripService.doSearch(this.origin, this.destination, this.departure_date)
                                      .subscribe((res) => {
                                        this.trips = res;
                                      });
  }

}
