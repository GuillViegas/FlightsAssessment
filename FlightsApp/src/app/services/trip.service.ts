import { Injectable } from '@angular/core';
import { Http, RequestOptions, Headers } from '@angular/http';
import { HttpParams } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class TripService {

  constructor(private http: Http) { }

  longestFlightDuration() {
      const headers = new Headers();
      headers.append('Content-Type', 'application/json');

      const options = new RequestOptions({ headers: headers });
      return this.http.get('http://localhost:8080/trip/longestflightduration', options).pipe(
              map((res) => {
                return res.json();
              });
            );
    }

  doSearch(origin, destination, departure_date) {
      let headers = new Headers();
      headers.append('Content-Type', 'application/json');

      let params = { "origin": origin,
                     "destination": destination,
                     "departure_date": departure_date };

      return this.http.get('http://localhost:8080/trip/dosearch', {headers: headers, params: params}).pipe(
          map((res) => {
            return res.json();
            });
          );
  }
}
