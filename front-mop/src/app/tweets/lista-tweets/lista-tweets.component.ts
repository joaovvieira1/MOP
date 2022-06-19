import { Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { TweetModel } from '../shared/tweet-model';

@Component({
  selector: 'app-lista-tweets',
  templateUrl: './lista-tweets.component.html',
  styleUrls: ['./lista-tweets.component.css']
})
export class ListaTweetsComponent implements OnInit {


  @Input() 
  public listaTweet: Observable<TweetModel[]> = new Observable<TweetModel[]>(); 

  constructor() { }

  ngOnInit(): void {
  }

}
