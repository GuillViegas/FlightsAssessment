import { Component, OnInit } from '@angular/core';
import { StateService } from '../../services/state.service';
import { RouteService } from '../../services/route.service';
import { TripService } from '../../services/trip.service';

@Component({
  selector: 'app-flights-summary',
  templateUrl: './flights-summary.component.html',
  styleUrls: ['./flights-summary.component.css']
})
export class FlightsSummaryComponent implements OnInit {
  longestkm = [];
  longestDuration = [];
  moreAirports;

  constructor(private routeService: RouteService,
              private stateService: StateService,
              private tripService: TripService) { }

  ngOnInit() {
    this.routeService.getLongestTripKM().subscribe((res) => {
      this.longestkm = res;
    });

    this.tripService.longestFlightDuration().subscribe((res) => {
      this.longestDuration = res;
    });

    this.stateService.getStateMostNumberOfAirports().subscribe((res) => {
      this.moreAirports = res;
    });
  }

}
