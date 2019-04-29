import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ExperimentalDataFormComponent } from './experimental-data-form.component';

describe('ExperimentalDataFormComponent', () => {
  let component: ExperimentalDataFormComponent;
  let fixture: ComponentFixture<ExperimentalDataFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ExperimentalDataFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ExperimentalDataFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
