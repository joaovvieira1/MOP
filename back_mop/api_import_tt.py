# Importando bibliotecas:
import tweepy as tw
import pandas as pd
import sqlite3
import complementos as comp


def salvarTweets():
    # Criando variaveis com as credenciais da API:
    bearer_token = comp.bearer_t
    consumer_key = comp.consumer_k
    consumer_secret = comp.consumer_s
    access_token = comp.access_t
    access_token_secret = comp.access_ts

    # Criando o Client:
    cliente = tw.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

    # Conectando ao BD SQLite3:
    con = sqlite3.connect('../../Jupyter/BD_a_eleicoes.db')

    cur = con.cursor()

    #Extraindo os TT:
    ttdados = cliente.search_recent_tweets(query = 'eleições -is:retweet', max_results = 100)

    dados = ttdados.data

    for i in dados:
        texto = i.text
        
        cur.execute("INSERT INTO tweets (texto, id_sentimento) VALUES (?,?)",(texto, 3))


    try:
        con.commit()
        con.close()
        return {'mensagem':'Sucesso'}
    except:
        con.close()
        return {'mensagem':'Deu ruim mané'}

