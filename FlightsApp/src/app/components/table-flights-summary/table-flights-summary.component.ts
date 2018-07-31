import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSort, MatPaginator, MatTableDataSource} from '@angular/material';
import { AirportService } from '../../services/airport.service';

@Component({
  selector: 'app-table-flights-summary',
  templateUrl: './table-flights-summary.component.html',
  styleUrls: ['./table-flights-summary.component.css']
})
export class TableFlightsSummaryComponent implements OnInit {
  displayedColumns: string[] = ['origin', 'nearest', 'min distance', 'farthest', 'max distance'];
  dataSource: MatTableDataSource<AirportStatistics>;
  airportStatistics = [];

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(private airportService: AirportService) {
  }

  ngAfterViewInit() {

    }

  ngOnInit() {
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
      this.airportStatistics = res;
      this.dataSource = new MatTableDataSource<AirportStatistics>(this.airportStatistics);
      this.dataSource.paginator = this.paginator;
      this.dataSource.sort = this.sort;
    });
  }
}

export interface AirportStatistics {
  origin: string;
  nearest: string;
  min_distance: number;
  farthest: string;
  max_distance: number;
}
