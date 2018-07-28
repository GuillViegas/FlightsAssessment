import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-flights-summary',
  templateUrl: './flights-summary.component.html',
  styleUrls: ['./flights-summary.component.css']
})
export class FlightsSummaryComponent implements OnInit {
  route = {'origin': 'BHZ', 'dest': 'BSB'};

  constructor() { }

  ngOnInit() {
  }

}
