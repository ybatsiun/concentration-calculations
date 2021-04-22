import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ChemicalEquationsFormComponent } from './chemical-equations-form.component';

describe('ChemicalEquationsFormComponent', () => {
  let component: ChemicalEquationsFormComponent;
  let fixture: ComponentFixture<ChemicalEquationsFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ChemicalEquationsFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChemicalEquationsFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
