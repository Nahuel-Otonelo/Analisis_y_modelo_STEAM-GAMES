import pandas as pd
import numpy as np
import ast
import json
from collections import Counter
rows = []


#df=pd.read_json('ETLJson.json')as

#def JPA(year: str):
 #   if type(year) != str:
  #      year = str(year)
   # data =  df.loc[df["release_date"].str.contains(year) == True]
    #data["app_name"].apply(lambda x: str (x))
    #data["release_date"].apply(lambda x: str(x))
    #data = data.dropna(subset=["app_name"])
    #names_list = [i for i in data["app_name"]]
    #return {year: names_list}




### Funcion genero( Año: str ):
#Se ingresa un año y devuelve una lista con los 5 géneros más ofrecidos en el orden correspondiente.

def gener(Año:str):
    df=pd.read_json('ETLJson.json')
    year=int(Año)
    df.dropna(subset=['genres'], inplace=True)
    df=df.loc[df['Year']== year]
    x=df['genres'].tolist()
    B=[]
    for lista1 in x:
        for numero in lista1:
            B.append(numero)
    dic = dict(Counter(B))
    dic = dict(sorted(dic.items(), reverse= True, key=lambda x:x[1])) # aqui es un diccionario
    lis=list(dic.keys())
    lis=lis[0:5]
    respuesta={year:lis}
    return(respuesta)


### Funcion juegos( Año: str ):
#Se ingresa un año y devuelve una lista con los juegos lanzados en el año.

def juegosna(Año: str):
    df = pd.read_json('ETLJson.json')
    df.drop(df.loc[df.app_name == 'no_info'].index, inplace=True)
    year = int(Año)
    df = df.loc[df['Year'] == year]
    x = df['app_name'].tolist()
    respuestaj={year: x }
    return respuestaj

## Funcion specs( Año: str ): 
#Se ingresa un año y devuelve una lista con los 5 specs que más se repiten en el mismo en el orden correspondiente.

def specsna(Año:str):
    df=pd.read_json('ETLJson.json')
    year=int(Año)
    df.dropna(subset=['specs'], inplace=True)
    df=df.loc[df['Year']== year]
    x=df['specs'].tolist()
    B=[]
    for lista1 in x:
        for numero in lista1:
            B.append(numero)
    dic = dict(Counter(B))
    dic = dict(sorted(dic.items(), reverse= True, key=lambda x:x[1])) # aqui es un diccionario
    lis=list(dic.keys())
    lis=lis[0:5]
    respuesta={year:lis}
    return(respuesta)



## Funcion earlyacces( Año: str ):
#Cantidad de juegos lanzados en un año con early access.

def earlyaccesna(Año: str):
    df=pd.read_json('ETLJson.json')
    year=int(Año)
    df.dropna(subset=['early_access'], inplace=True)
    df=df.loc[df['Year']== year]
    df=df.loc[df['early_access']== True]
    x = df['early_access'].tolist()
    return (len(x))


## Funcion sentiment( Año: str ): 
## Según el año de lanzamiento, se devuelve una lista con la cantidad de registros que se encuentren categorizados con un análisis de sentimiento.

def sentimentna(Año: str):
    df=pd.read_json('ETLJson.json')
    year=int(Año)
    df.drop(df.loc[df.sentiment == 'no_info'].index, inplace=True)
    df=df.loc[df['Year']== year]
    sentiments=df['sentiment'].tolist()

    dic = dict(Counter(sentiments))
    dic = dict(sorted(dic.items(), reverse= True, key=lambda x:x[1])) # aqui es un diccionario
    return dic


## Funcion metascore( Año: str ):
#Top 5 juegos según año con mayor metascore.

