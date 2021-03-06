import { Injectable } from '@angular/core';
import { Http, RequestOptions, Headers } from '@angular/http';
import { map } from 'rxjs/operators';

@Injectable()
export class AirportService {

  constructor(private http: Http) { }

  getAiportStatistics() {
  		const headers = new Headers();
    	headers.append('Content-Type', 'application/json');

    	const options = new RequestOptions({ headers: headers });
	    return this.http.get('http://localhost:8080/airport/getairportstatistics', options).pipe(
	            map((res) => {
	              return res.json();
              })
            );
  	}

    getAllAirports() {
        const headers = new Headers();
        headers.append('Content-Type', 'application/json');

        const options = new RequestOptions({ headers: headers });
        return this.http.get('http://localhost:8080/airport/getallairports', options).pipe(
                map((res) => {
                  return res.json();
                })
              );
      }
}
