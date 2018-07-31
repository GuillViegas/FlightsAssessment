import { Injectable } from '@angular/core';
import { Http, RequestOptions, Headers } from '@angular/http';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class StateService {

  constructor(private http: Http) { }

  getStateMostNumberOfAirports() {
      const headers = new Headers();
      headers.append('Content-Type', 'application/json');

      const options = new RequestOptions({ headers: headers });
      return this.http.get('http://localhost:8080/state/getstatemostnumberairports', options).pipe(
              map((res) => {
                return res.json();
              })
            );
    }
}
