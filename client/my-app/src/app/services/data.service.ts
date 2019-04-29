import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private differentialEquationsSystem = new BehaviorSubject('default message');
  currentDifferentialEquationsSystem = this.differentialEquationsSystem.asObservable();

  constructor() { }

  changeMessage(system: string) {
    this.differentialEquationsSystem.next(system)
  }

}