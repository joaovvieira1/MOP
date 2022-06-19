#Importar bibliotecas e conectar banco:

import json
import sqlite3
import sys
import numpy as np #Algebra Linear
import pandas as pd #Processamento de dados
import re #Cadeia de caracteres 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.metrics import accuracy_score
import pickle
import complementos as comp

con = sqlite3.connect('../../Jupyter/BD_a_eleicoes.db')
cur = con.cursor()

data = comp.select_valor()

#Removendo Tags html:
def clean(text):
    cleaned = re.compile(r'<.*?>')
    return re.sub(cleaned,'',text)

#Removendo caracteres especiais:
def is_special(text):
    rem = ''
    for i in text:
        if i.isalnum():
            rem = rem + i
        else:
            rem = rem + ' '
    return rem

#Convertendo todas as letras para minuscula:
def to_lower(text):
    return text.lower()

#Removendo palavras inuteis:
import nltk
nltk.download('stopwords')
nltk.download('punkt')

def rem_stopwords(text):
    stop_words = set(stopwords.words('portuguese'))
    stop_words.add('eleicao')
    stop_words.add('lula')
    stop_words.add('bolsonaro')
    words = word_tokenize(text)
    return [w for w in words if w not in stop_words]


def stem_txt(text):
    ss = SnowballStemmer('portuguese')
    return " ".join([ss.stem(w) for w in text])


cv = CountVectorizer(max_features = 1000) 
bnb = BernoulliNB(alpha=1.0,fit_prior=True)


def treinar():
    data.texto = data.texto.apply(clean)
    data.texto = data.texto.apply(is_special)
    data.texto = data.texto.apply(to_lower)
    data.texto = data.texto.apply(rem_stopwords)
    data.texto = data.texto.apply(stem_txt)

    #criação da maquina preditiva:
    x = np.array(data.iloc[:,0].values)
    y = np.array(data.valor.values)

    x = cv.fit_transform(data.texto).toarray()

    # treino e teste:
    trainx,testx,trainy,testy = train_test_split(x, y, test_size=0.2,random_state=9)
    
    #Modelos de treinamento:
    bnb.fit(trainx,trainy)

    #Predição e acurracia dos modelos:
    ypb = bnb.predict(testx)

    return(json.dumps({'acuracia': accuracy_score(testy,ypb)}))




#EXECUTA O TREINAR
treinar()

#Consumir ML:
def analisarIndeferentes():
    rev = comp.select_ind()
    rev = rev.reset_index() 

    for index, row in rev.iterrows():
        f1 = clean(row['texto'])
        f2 = is_special(f1)
        f3 = to_lower(f2)
        f4 = rem_stopwords(f3)
        f5 = stem_txt(f4)
        print(f5, file=sys.stderr)        


        bow,words = [],word_tokenize(f5)
        for word in words:
            bow.append(words.count(word))

        word_dict = cv.vocabulary_
        pickle.dump(word_dict,open('MOP_v1.pkl','wb'))

        inp = []
        for i in word_dict:
            inp.append(f5.count(i[0]))
        y_pred = bnb.predict(np.array(inp).reshape(1,1000))
        retornostr = ''
        retornostr = ' '.join(map(str, y_pred))

        if( retornostr == 'bom' ):
            comp.update_sentimento(row['id'], 1)
            print("Positivo", file=sys.stderr)        

        if (retornostr == 'ruim'):
            comp.update_sentimento(row['id'], 2)
            print("Nrgativo", file=sys.stderr)        

    return 0
    
