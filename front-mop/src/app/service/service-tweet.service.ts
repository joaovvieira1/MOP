import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { TweetModel } from '../tweets/shared/tweet-model';

@Injectable({
  providedIn: 'root'
})
export class TweetService {

  constructor(private httpService: HttpClient
  ) {
  }

  public carregarTweet() {
    return this.httpService.get('/listarTweets');
  }

  public carregarMaisTweet() {
    return this.httpService.post('/salvarTweets', {});
  }

  public carregarNegativos() {
    return this.httpService.get('/consultar-ruim')
  }

  public carregarPositivos() {
    return this.httpService.get('/consultar-bom')
  }

  public carregarQuantidadePositivos() {
    return this.httpService.get('/consultar-quantidade-bom')
  }
  
  public carregarQuantidadeNegativos() {
    return this.httpService.get('/consultar-quantidade-ruim')
  }

  public analisarIndefinidos() {
    return this.httpService.get('/analisar-indefinidos')
  }

  public carregarAcuracia() {
    return this.httpService.get('/consultar-acuracia')
  }
}
