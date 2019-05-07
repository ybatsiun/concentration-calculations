import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private differentialEquationsSystem = new BehaviorSubject([]);
  currentDifferentialEquationsSystem = this.differentialEquationsSystem.asObservable();

  constructor() { }

  changeMessage(system: Array <String>) {
    this.differentialEquationsSystem.next(system)
  }

}