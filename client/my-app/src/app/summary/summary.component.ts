import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';




@Component({
  selector: 'app-summary',
  templateUrl: './summary.component.html',
  styleUrls: ['./summary.component.css']
})
export class SummaryComponent implements OnInit {
  summary;
  constructor(private data: DataService) { }

  ngOnInit() {
    this.data.currentSummary.subscribe(summary => {
      this.summary = summary['text'];
    })
  };
};
