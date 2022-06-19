import sqlite3
import pandas as pd


#Credencias de acessp Twitter:
bearer_t = 'AAAAAAAAAAAAAAAAAAAAABj5bwEAAAAAheuvXYm%2FADRjy9NU5JObyDVTfO8%3DUcQuFVcCWBuMOiZWkzi8SjJLxyaRsnccODOJfFEOIZjuuKMzfS'
consumer_k = '0YLmSe9g02nH0sS7MmhNPk5vP'
consumer_s = 'B21vIEolKWnk0w21HP7o50iJZDqXH4D7ftT12XJT7qZIBbf18b'
access_t = '1197655981624373248-wtNV3uWa9nJoUznCPvMtmIn41Qh9HM'
access_ts = '8fhGA2owrxxWzGO2EzhWCoZs1xWt7kjywAxFahGvo2C6e'

#Funções de extração seletiva:
    #Valores diferentes de 3:
def select_valor():
    con = sqlite3.connect('../../Jupyter/BD_a_eleicoes.db')
    data = pd.read_sql_query('SELECT tweets.texto, sentimentos.valor FROM tweets, sentimentos WHERE tweets.id_sentimento = sentimentos.id_sentimento and sentimentos.id_sentimento != 3',con)
    return(data)

    #Valores iguais a 3:
def select_ind():
    con = sqlite3.connect('../../Jupyter/BD_a_eleicoes.db')
    rev = pd.read_sql_query('SELECT tweets.id_tweets as id, tweets.texto as texto, sentimentos.valor as valor FROM tweets, sentimentos WHERE tweets.id_sentimento = sentimentos.id_sentimento and sentimentos.id_sentimento == 3',con)
    con.close()
    return(rev)

    #Valores iguais a 1
def select_bom():
    con = sqlite3.connect('../../Jupyter/BD_a_eleicoes.db')
    rev = pd.read_sql_query('SELECT tweets.texto as texto, sentimentos.valor as valor FROM tweets, sentimentos WHERE tweets.id_sentimento = sentimentos.id_sentimento and sentimentos.id_sentimento == 1 ORDER BY tweets.id_tweets DESC',con)
    con.close()
    return(rev)
    
    #Valores iguais a 2
def select_ruim():
    con = sqlite3.connect('../../Jupyter/BD_a_eleicoes.db')
    rev = pd.read_sql_query('SELECT tweets.texto, sentimentos.valor FROM tweets, sentimentos WHERE tweets.id_sentimento = sentimentos.id_sentimento and sentimentos.id_sentimento == 2 ORDER BY tweets.id_tweets DESC',con)
    con.close()
    return(rev)

#Funções para calculo de grafico:
def sum_bom():
    con = sqlite3.connect('../../Jupyter/BD_a_eleicoes.db')
    cur = con.cursor()
    sum = pd.read_sql_query('SELECT COUNT(id_sentimento) as quantidade FROM tweets WHERE id_sentimento = "1" ',con)
    con.close()
    return(sum)

def sum_ruim():
    con = sqlite3.connect('../../Jupyter/BD_a_eleicoes.db')
    cur = con.cursor()
    sub = pd.read_sql_query('SELECT COUNT(id_sentimento) as quantidade FROM tweets WHERE id_sentimento = "2" ',con)
    con.close()
    return(sub)

def update_sentimento(id_tweet, id_sentimento):
    con = sqlite3.connect('../../Jupyter/BD_a_eleicoes.db')
    cur = con.cursor()
    cur.execute("UPDATE tweets SET id_sentimento = ? WHERE id_tweets = ?",(id_sentimento, id_tweet))
    con.commit()
    con.close()



