import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";

@Component({
  selector: 'app-experimental-data-form',
  templateUrl: './experimental-data-form.component.html',
  styleUrls: ['./experimental-data-form.component.css']
})
export class ExperimentalDataFormComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }

  run(){
    // do some logic
    this.router.navigateByUrl('/summary');
  }

}
