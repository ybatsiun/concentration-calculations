import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { FormBuilder, FormGroup, FormArray, FormControl, Validators } from '@angular/forms';


@Component({
  selector: 'app-chemical-equations-form',
  templateUrl: './chemical-equations-form.component.html',
  styleUrls: ['./chemical-equations-form.component.css']
})
export class ChemicalEquationsFormComponent implements OnInit {
  equationsForm: FormGroup;
  equationCtrl: FormControl;

  constructor(private router: Router, private fb: FormBuilder) { }

  ngOnInit() {
    //TODO make full reaction validation
    this.equationCtrl = this.fb.control('', Validators.compose([Validators.required, Validators.pattern(/(\+|->|=)/)]));

    this.equationsForm = this.fb.group({
      equations: this.fb.array([this.fb.group({ equation: this.equationCtrl })])
    })
  }

  get equationsGetter() {
    return this.equationsForm.get('equations') as FormArray;
  }

  addEquation() {
    this.equationsGetter.push(this.fb.group({ equation: '' }));
  }

  deleteEquation(index) {
    this.equationsGetter.removeAt(index);
  }

  getDifferentialEquations() {
    //do some logic
    this.router.navigateByUrl('/configConstants');
  }

}


class Equations {

  constructor(
    public equation: string,
  ) { }
}