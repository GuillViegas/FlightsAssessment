import { Component, OnInit } from '@angular/core';


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

  constructor() { }

  ngOnInit() {
  }

}
