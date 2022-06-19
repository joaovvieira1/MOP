import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TweetsComponent } from './tweets.component';
import { ListaTweetsComponent } from './lista-tweets/lista-tweets.component';
import { NgxChartsModule } from '@swimlane/ngx-charts';



@NgModule({
  declarations: [
    TweetsComponent,
    ListaTweetsComponent,
  ],
  imports: [
    CommonModule,
    NgxChartsModule

  ],
  exports:[TweetsComponent]
})
export class TweetsModule { }
