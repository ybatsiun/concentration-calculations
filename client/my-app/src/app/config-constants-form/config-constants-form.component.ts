import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { DataService } from '../services/data.service';
import { FormBuilder, FormGroup, FormArray, FormControl, Validators } from '@angular/forms';




@Component({
  selector: 'app-config-constants-form',
  templateUrl: './config-constants-form.component.html',
  styleUrls: ['./config-constants-form.component.css']
})
export class ConfigConstantsFormComponent implements OnInit {
  htmlConstants; initialConcentrations; constantControl: FormControl;

  configForm;

  constructor(private router: Router, private data: DataService, private fb: FormBuilder) { }

  ngOnInit() {
    this.getConstants();
  }

  getConstants() {
    this.data.currentDifferentialEquationsSystem.subscribe(message => {
      let rawHtml = message.map(e => e.html).toString();
      this.htmlConstants = rawHtml.match(/k<sub>\d<\/sub>/g).filter((value, index, self) => {
        return self.indexOf(value) === index;
      });

      this.configForm = this.fb.group({
        speedConstants: this.fb.array([])
      });

      for (let i = 0; i < this.htmlConstants.length; ++i) {
        this.addConstant();
      };

    });
  };

  get speedConstants() {
    return this.configForm.get('speedConstants') as FormArray;
  };

  addConstant() {
    this.speedConstants.push(this.fb.group({
      min: this.fb.control(''),
      max: this.fb.control(''),
      step: this.fb.control('')
    }));
  };



}
