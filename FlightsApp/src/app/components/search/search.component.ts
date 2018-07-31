import { Component, OnInit } from '@angular/core';
import { AirportService } from '../../services/airport.service';


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
  origin;
  destination;
  airports: Airport[] = [
    {iata: 'BHZ', city: 'Belo Horizonte'},
    {iata: 'BSB', city: 'Brasília'}
  ];

  constructor(private airportService: AirportService) { }

  ngOnInit() {
    this.getAllAirports();
  }

  getAllAirports(){
    this.airportService.getAllAirports().subscribe((res) => {
      this.airports = res;
    });
  }

}
