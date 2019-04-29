import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";

@Component({
  selector: 'app-config-constants-form',
  templateUrl: './config-constants-form.component.html',
  styleUrls: ['./config-constants-form.component.css']
})
export class ConfigConstantsFormComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }

}
