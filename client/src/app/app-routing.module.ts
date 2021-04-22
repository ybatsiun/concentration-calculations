import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ChemicalEquationsFormComponent } from './chemical-equations-form/chemical-equations-form.component';
import { ConfigConstantsFormComponent } from './config-constants-form/config-constants-form.component';
import { ExperimentalDataFormComponent } from './experimental-data-form/experimental-data-form.component';
import { SummaryComponent } from './summary/summary.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';


const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: WelcomeComponent },
  { path: 'chemicalEquations', component: ChemicalEquationsFormComponent },
  { path: 'configConstants', component: ConfigConstantsFormComponent },
  { path: 'experimentalData', component: ExperimentalDataFormComponent },
  { path: 'summary', component: SummaryComponent },
  { path: '**', component: PageNotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
