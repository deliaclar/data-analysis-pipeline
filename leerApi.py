import requests
import pandas as pd
from itertools import chain
from IPython.display import Image
from IPython.core.display import HTML
from IPython.display import display, Image


def createDict(ids, url): 
	dic=dict()#recorremos los ids de los pokemons
	#los añadimos a la url común para obtener los datos de cada pokemon
	for e in ids:
		res=requests.get(url+str(e)).json()
		list=[]
		for e in res.get("abilities"): #Una vez echo esto cogemos las habilidades de cada uno
			list.append(e.get("ability").get("name"))
		dic[res.get("id")]=[res.get("height"),list] #añadimos junto con el id del pokemon
    	#su altura y la lista creada anteriormente 
	return dic


def crearDataFrame(dic):
	#CREAMOS EL DATAFRAME CON LOS ELEMENTOS RECIEN SACADOS DE LA API
	lista=[x for x in chain.from_iterable(dic.values())] #LISTA DE LOS VALORES
	ids=[x for x in dic.keys()]#LISTA DE LOS IDS
	ht=[]
	a1=[]
	a2=[]
	a3=[]
	i=0
	while i<len(lista):
		ht.append(lista[i])
		a1.append(lista[i+1][0])
		try:
			a2.append(lista[i+1][1])
		except Exception:
			a2.append("None") #SI NO HAY HABILIDAD , AÑADIREMOS UN NONE
		try:
			a3.append(lista[i+1][2])
		except Exception:
			a3.append("None") 
		i+=2
		data={
			"ID": ids,
			"Height":ht,
			"Ability1":a1,
			"Ability2":a2,
			"Ability3":a3
		}
	return pd.DataFrame(data) 

def dataPokemon(df,pokemon):
	result = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon.lower()))
	result=result.json()
	display(df[df["Name"]==pokemon.capitalize()])
	img=Image(url=result["sprites"]["front_default"])
	#img.show()