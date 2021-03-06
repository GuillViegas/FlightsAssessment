import { Injectable } from '@angular/core';
import { Http, RequestOptions, Headers } from '@angular/http';
import { map } from 'rxjs/operators';

@Injectable()
export class RouteService {

  constructor(private http: Http) { }

  getLongestTripKM() {
      const headers = new Headers();
      headers.append('Content-Type', 'application/json');

      const options = new RequestOptions({ headers: headers });
      return this.http.get('http://localhost:8080/route/getlongesttripkm', options).pipe(
              map((res) => {
                return res.json();
              })
            );
    }
}
