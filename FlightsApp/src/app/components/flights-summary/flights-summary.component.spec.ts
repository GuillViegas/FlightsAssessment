import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FlightsSummaryComponent } from './flights-summary.component';

describe('FlightsSummaryComponent', () => {
  let component: FlightsSummaryComponent;
  let fixture: ComponentFixture<FlightsSummaryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FlightsSummaryComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FlightsSummaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
