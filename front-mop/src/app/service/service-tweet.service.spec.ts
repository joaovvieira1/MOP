import { TestBed } from '@angular/core/testing';

import { TweetService } from './service-tweet.service';

describe('ServiceTweetService', () => {
  let service: TweetService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TweetService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('deve carregar novos tweets', () => {
    const lista = service.carregarMaisTweet()
    expect(lista).toHaveSize(100)
  })
});
