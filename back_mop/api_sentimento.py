import json
from flask import Flask
from api_analysis_tt import analisarIndeferentes, treinar
from api_list_tt import listar
from api_import_tt import salvarTweets
import complementos

api = Flask("api_mpo")

@api.route('/salvarTweets', methods=['POST'])
def salvar():
    return salvarTweets()
    

@api.route('/listarTweets', methods=['GET'])
def getTweets():
    return listar()

@api.route('/consultar-valores', methods=['GET'])
def getValores():
    dados =  complementos.select_valor()
    result = dados.to_json(orient="records")
    parsed = json.loads(result)
    return (json.dumps(parsed, indent=4))

@api.route('/consultar-bom', methods=['GET'])
def getBom():
    dados =  complementos.select_bom()
    result = dados.to_json(orient="records")
    parsed = json.loads(result)
    return (json.dumps(parsed, indent=4))

@api.route('/consultar-ruim', methods=['GET'])
def getRuim():
    dados =  complementos.select_ruim()
    result = dados.to_json(orient="records")
    parsed = json.loads(result)
    return (json.dumps(parsed, indent=4))

@api.route('/consultar-quantidade-bom', methods=['GET'])
def getSumBom():
    dados =  complementos.sum_bom()
    result = dados.to_json(orient="records")
    parsed = json.loads(result)
    return (json.dumps(parsed, indent=4))

@api.route('/consultar-quantidade-ruim', methods=['GET'])
def getSumRuim():
    dados =  complementos.sum_ruim()
    result = dados.to_json(orient="records")
    parsed = json.loads(result)
    return (json.dumps(parsed, indent=4))

@api.route('/analisar-indefinidos', methods=['GET'])
def analisarTweetsIndefinidos():
    dados = analisarIndeferentes()

    return (json.dumps(dados, indent=4))

@api.route('/consultar-acuracia', methods=['GET'])
def consultarAcuracia():
    return treinar()


api.run()