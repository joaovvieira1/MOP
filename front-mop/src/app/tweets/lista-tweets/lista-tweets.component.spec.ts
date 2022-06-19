import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaTweetsComponent } from './lista-tweets.component';

describe('ListaTweetsComponent', () => {
  let component: ListaTweetsComponent;
  let fixture: ComponentFixture<ListaTweetsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListaTweetsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ListaTweetsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
