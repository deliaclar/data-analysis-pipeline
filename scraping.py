from bs4 import BeautifulSoup
from selenium import webdriver
import requests

def crearColumna(nombres,url):
    categoria=[]
    for e in nombres:
        soup=BeautifulSoup(requests.get(url+str(e).lower()).text,"html.parser")
        sel=soup.select(".pokemon-ability-info .push-7 ul li .attribute-value")
        try:
            categoria.append(sel[0].text)
        except Exception:
            categoria.append("None")

    return categoria