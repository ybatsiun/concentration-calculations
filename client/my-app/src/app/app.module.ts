import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { WelcomeComponent } from './welcome/welcome.component';
import { ChemicalEquationsFormComponent } from './chemical-equations-form/chemical-equations-form.component';
import { ConfigConstantsFormComponent } from './config-constants-form/config-constants-form.component';
import { ExperimentalDataFormComponent } from './experimental-data-form/experimental-data-form.component';
import { SummaryComponent } from './summary/summary.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';

@NgModule({
  declarations: [
    AppComponent,
    WelcomeComponent,
    ChemicalEquationsFormComponent,
    ConfigConstantsFormComponent,
    ExperimentalDataFormComponent,
    SummaryComponent,
    PageNotFoundComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }