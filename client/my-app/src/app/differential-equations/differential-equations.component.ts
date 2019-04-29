import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';


@Component({
  selector: 'app-differential-equations',
  templateUrl: './differential-equations.component.html',
  styleUrls: ['./differential-equations.component.css']
})
export class DifferentialEquationsComponent implements OnInit {
  message

  constructor(private data: DataService) { }
  ngOnInit() {
    this.data.currentDifferentialEquationsSystem.subscribe(message => this.message = message)
  }

}
