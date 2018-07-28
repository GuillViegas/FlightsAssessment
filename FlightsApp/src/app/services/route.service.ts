import { Injectable } from '@angular/core';
import { Http, RequestOptions, Headers } from '@angular/http';

@Injectable()
export class RouteService {

  constructor(private http: Http) { }
}
