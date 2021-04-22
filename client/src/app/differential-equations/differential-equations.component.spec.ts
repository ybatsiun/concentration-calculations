import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DifferentialEquationsComponent } from './differential-equations.component';

describe('DifferentialEquationsComponent', () => {
  let component: DifferentialEquationsComponent;
  let fixture: ComponentFixture<DifferentialEquationsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DifferentialEquationsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DifferentialEquationsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
