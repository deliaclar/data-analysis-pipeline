#IMPORTAMOS LAS LIBRERARIAS QUE VAMOS A NECESITAR
import pandas as pd
import requests
import numpy as np
from itertools import chain
from bs4 import BeautifulSoup
from selenium import webdriver
import matplotlib.pyplot as plt
from IPython.display import Image
from IPython.core.display import HTML
import leerApi
import scraping
import graficas
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
	df2=pd.leerApi.crearDataFrame(d2)
    #Ahora juntamos df1 y df2 al df total
    return pd.merge(df,pd.concat([df1,df2]),on="ID")


def anadirDatosWeb(url,res):
    res["Categoria"]=scraping.crearColumna(res.Name.values,url)
    return res

def representarGraficas(data):
    #Representación de las gráficas
	graficas.representacionGrafica(data,"Attack","Defense","Relación del poder de defensa junto al de ataque")
	graficas.representacionGrafica(data,"Defense","Height","Relación de la altura con el poder de defensa")
	graficas.representacionGrafica(data,"Legendary","Attack","Poder de ataque dividido por pokemons legendarios o no")

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
    res=anadirDatosWeb(res,"https://www.pokemon.com/es/pokedex/")
    #Representación de las gráficas
    representarGraficas(res)
	datoPokemon(res)
	

if __name__=="__main__":
	main()
