import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { DataService } from '../services/data.service';
import { FormBuilder, FormGroup, FormArray, FormControl, Validators } from '@angular/forms';
import { HttpClientService } from '../services/http-client.service';

@Component({
  selector: 'app-config-constants-form',
  templateUrl: './config-constants-form.component.html',
  styleUrls: ['./config-constants-form.component.css']
})
export class ConfigConstantsFormComponent implements OnInit {
  htmlConstants; constantControl: FormControl; configForm; reagents;

  constructor(private router: Router, private data: DataService, private fb: FormBuilder, private httpCLient: HttpClientService) { }

  ngOnInit() {
    this.getConstants();
  };

  getConstants() {
    this.data.currentDifferentialEquationsSystem.subscribe(message => {
      let rawHtml = message.map(e => e.html).toString();
      this.reagents = message.map(e => e.reagent);
      this.htmlConstants = rawHtml.match(/k<sub>\d<\/sub>/g).filter((value, index, self) => {
        return self.indexOf(value) === index;
      });

      this.configForm = this.fb.group({
        speedConstants: this.fb.array([]),
        calculationConfig: this.fb.group({
          initialConcentrations: this.fb.array([]),
          timeInterval: this.fb.group({
            start: this.fb.control(''),
            finish: this.fb.control('')
          }),
          partsToDivide: this.fb.control('')
        }),
        experimantalData: this.fb.control('')
      });

      for (let i = 0; i < this.htmlConstants.length; i++) {
        this.addConstant();
      };

      this.reagents.forEach(element => {
        this.addInitialConcentration(element);
      });

    });
  };
  get initialConcentrations() {
    return this.configForm.get('calculationConfig').get('initialConcentrations') as FormArray;
  };

  addInitialConcentration(reagentName) {
    this.initialConcentrations.push(this.fb.group({
      [reagentName]: this.fb.control('')
    }));
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

  onSubmit() {
    this.configForm.value.calculationConfig.timeInterval =
      [this.configForm.value.calculationConfig.timeInterval.start,
      this.configForm.value.calculationConfig.timeInterval.finish];
    this.httpCLient.calculateConstants(this.configForm.value).subscribe(summary => {
      //TODO handle error
      this.data.changeMessage(summary)
      this.router.navigateByUrl('/summary');
    }
    );
  };
}
