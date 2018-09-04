#coding: utf-8

from lxml import html 
from lxml import etree
import pandas as pd

if __name__ == "__main__":

    arquivo = open('mulheres_palestrantes.htm',mode="r", encoding="utf-8").read()
    pagina = etree.HTML(arquivo)
    
    nomes = pagina.xpath('//article[@class="card"]/h3/text()')
    fotos = pagina.xpath('//article[@class="card"]/img/@src')
    localizacoes = pagina.xpath('//article[@class="card"]/div/p[@class="location"]/text()')

    participantes = []
    
    for nome,foto,localizacao in zip(nomes,fotos,localizacoes):
        participantes.append((nome, foto, localizacao))

print (participantes)
