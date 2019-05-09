import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private differentialEquationsSystem = new BehaviorSubject([]);
  currentDifferentialEquationsSystem = this.differentialEquationsSystem.asObservable();
  private summary = new BehaviorSubject([]);
  currentSummary = this.summary.asObservable();

  constructor() { }

  changeMessage(system: Array <String>) {
    this.differentialEquationsSystem.next(system);
  }

  setSummary(text:any) {
    this.summary.next(text);
  }

}