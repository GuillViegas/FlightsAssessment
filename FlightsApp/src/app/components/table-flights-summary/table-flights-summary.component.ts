import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSort, MatPaginator, MatTableDataSource} from '@angular/material';
import { AirportService } from '../../services/airport.service';

@Component({
  selector: 'app-table-flights-summary',
  templateUrl: './table-flights-summary.component.html',
  styleUrls: ['./table-flights-summary.component.css']
})
export class TableFlightsSummaryComponent implements OnInit {
  displayedColumns: string[] = ['iata', 'city', 'state' ];
  dataSource: MatTableDataSource<Airport>;
  aiports = [];

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(private airportService: AirportService) {
    this.dataSource = new MatTableDataSource<Airport>(AIRPORT_DATA);
  }

  ngOnInit() {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
    this.getAiportStatistics();
  }

  applyFilter(filterValue: string) {
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  getAiportStatistics(){
    this.airportService.getAiportStatistics().subscribe((res) => {
      this.aiports = res;
    });
  }
}

export interface Airport {
  iata: string;
  city: string;
  state: string;
}

const AIRPORT_DATA: Airport[] = [
  {iata: "AAX", city: "Araxa", state: "MG"},
  {iata: "AFL", city: "Alta Floresta", state: "MT"},
  {iata: "AJU", city: "Aracaju", state: "SE"},
  {iata: "AQA", city: "Araraquara", state: "SP"},
  {iata: "ARU", city: "Aracatuba", state: "SP"},
  {iata: "ATM", city: "Altamira", state: "PA"}
];
