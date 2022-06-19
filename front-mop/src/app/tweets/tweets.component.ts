import { Component, OnInit } from '@angular/core';
import { TweetService } from '../service/service-tweet.service';
import { TweetModel } from './shared/tweet-model';

@Component({
  selector: 'app-tweets',
  templateUrl: './tweets.component.html',
  styleUrls: ['./tweets.component.css']
})
export class TweetsComponent implements OnInit {

  constructor(
    private serviceTweet: TweetService
  ) { }

  public tweets: Array<TweetModel> = new Array<TweetModel>();

  public listaTweetsPositivo: any;
  public listaTweetsNegativo: any;
  public quantidadeNegativo: number = 0;
  public quantidadePositivo: number = 0;
  public acuracia: number = 0;
  public cores: any =
    [
      { name: "Bom", value: '#11e809' },
      { name: "Ruim", value: '#f70202' },
    ]
  public dados: Array<any> = [
    {
      name: "Bom",
      value: 0
    },
    {
      name: "Ruim",
      value: 0
    }
  ]


  ngOnInit(): void {
    this.carregarAcuracia();
    this.carregarNegativo();
    this.carregarQuantidades();
    this.carregarPositivo();

  }

  carregarMaisTweet() {
    this.serviceTweet.carregarMaisTweet().subscribe();
    window.location.reload();
  }


  carregarPositivo() {
    this.listaTweetsPositivo = this.serviceTweet.carregarPositivos();

  }
  carregarNegativo() {
    this.listaTweetsNegativo = this.serviceTweet.carregarNegativos();


  }

  carregarQuantidades() {
    this.serviceTweet.carregarQuantidadePositivos().subscribe(
      (resposta: any = [{ quantidade: 0 }]) => {
        this.quantidadePositivo = resposta[0].quantidade
        this.dados[0].value = this.quantidadePositivo
        this.dados = [...this.dados];

     })

    this.serviceTweet.carregarQuantidadeNegativos().subscribe(
      (resposta: any = { quantidade: 0 }) => {
        this.quantidadeNegativo = resposta[0].quantidade
        this.dados[1].value = this.quantidadeNegativo

        this.dados = [...this.dados];
        
      })
  }

  analisarIndefinidos() {
    this.serviceTweet.analisarIndefinidos().subscribe((resposta) => console.log(resposta)
    )
    
    window.location.reload();
  }

  carregarAcuracia() {
    this.serviceTweet.carregarAcuracia().subscribe((resposta: any = { acuracia: 0 }) => this.acuracia = resposta.acuracia)
  }



}
