#IMPORTAMOS LAS LIBRERARIAS QUE VAMOS A NECESITAR
import pandas as pd
import requests
import numpy as np

import music
import leerApi
import scraping
import graficas
import pdf
import leerDatos as ld

def leerDatos(file):
    return ld.readData(file)

def anadirDatosApi(df,url):
    #He dividido en dos los ids porque al practicar con jupyter notebook
	#se me atascaba si los hacia de golpe en una misma celda
    ids=df["#"].values
    d=leerApi.createDict(ids[0:int(len(ids)/2)],url)
    df1=leerApi.crearDataFrame(d)
    #HACEMOS LO MISMO CON LA SEGUNDA MITAD DE LOS DATOS
    d2=leerApi.createDict(ids[int(len(ids)/2):],url)
    df2=leerApi.crearDataFrame(d2)
    #Ahora juntamos df1 y df2 al df total
    df.rename(columns={"#":"ID"},inplace=True)
    return pd.merge(df,pd.concat([df1,df2]),on="ID")

    
def anadirDatosWeb(res,url):
    res["Categoria"]=scraping.crearColumna(res.Name.values,url)
    return res

def representarGraficas(data):
    #Representación de las gráficas
	graficas.representacionGrafica(data,"Attack","Defense","Relación del poder de defensa junto al de ataque",0)
	graficas.representacionGrafica(data,"Defense","Height","Relación de la altura con el poder de defensa",1)
	graficas.representacionGrafica(data,"Legendary","Attack","Poder de ataque dividido por pokemons legendarios o no",2)

def datoPokemon(data):
    #Pedimos el pokemon del cual queremos saber su información
	pokemon=input("Introduzca el pokemon deseado: ")
	leerApi.dataPokemon(data,pokemon)

def main():
    #LEEMOS LOS DATOS DE NUESTRO CSV
    df = leerDatos("Pokemon.csv")
    #AÑADIMOS LOS DATOS DE LA API 
    res=anadirDatosApi(df,"https://pokeapi.co/api/v2/pokemon/")
    #AÑADIMOS LOS DATOS DE LA WEB
    url='https://www.pokemon.com/es/pokedex/'
    res=anadirDatosWeb(res,url)
    #Representación de las gráficas
    representarGraficas(res)
    datoPokemon(res)
    pdf.creoPDF()
    music.soundMusic()
	

if __name__=="__main__":
	main()
