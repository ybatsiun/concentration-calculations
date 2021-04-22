import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ConfigConstantsFormComponent } from './config-constants-form.component';

describe('ConfigConstantsFormComponent', () => {
  let component: ConfigConstantsFormComponent;
  let fixture: ComponentFixture<ConfigConstantsFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ConfigConstantsFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ConfigConstantsFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
