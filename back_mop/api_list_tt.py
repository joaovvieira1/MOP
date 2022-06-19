# Importando bibliotecas:
import pandas as pd
import sqlite3
import json

def listar():
    # Conectando ao BD SQLite3:
    con = sqlite3.connect('../../Jupyter/BD_a_eleicoes.db')
    cur = con.cursor()

    cur.execute('SELECT texto FROM tweets')
    resposta = cur.fetchall()
    resposta = pd.DataFrame(resposta)

    resposta.columns = ['texto']
    result = resposta.to_json(orient="records")
    parsed = json.loads(result)

    con.close()
    return(json.dumps(parsed, indent=4))

