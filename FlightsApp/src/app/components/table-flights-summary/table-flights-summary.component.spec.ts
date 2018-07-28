import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TableFlightsSummaryComponent } from './table-flights-summary.component';

describe('TableFlightsSummaryComponent', () => {
  let component: TableFlightsSummaryComponent;
  let fixture: ComponentFixture<TableFlightsSummaryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TableFlightsSummaryComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TableFlightsSummaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
