#coding: utf-8
import sqlite3

from lxml import html
from lxml import etree

connection = sqlite3.connect('mulheres.db')
c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS mp (nome, foto, localizacao)')

create_table()

def inserir_dados (participantes):
    c.execute('INSERT INTO mp (nome, foto, localizacao)')
    
   
    
    


if __name__ == "__main__":

    arquivo = open('mulheres_palestrantes_certo.htm', encoding = 'utf-8').read()
    pagina = etree.HTML(arquivo)

    nomes = pagina.xpath('//article[@class="card"]/h3/text()')
    fotos = pagina.xpath('//article[@class="card"]/img/@src')
    localizacoes = pagina.xpath('//article[@class="card"]/div/p[@class="location"]/text()')

    participantes = []

    for nome, foto, localizacao in zip(nomes, fotos, localizacoes):
        participante = {'nome': nome, 'foto': foto, 'localizacao': localizacao}
        participantes.append(participante)
        inserir_dados(participante)
        
        
    print (participantes)

    
    '''
    cards = pagina.xpath('//article[@class="card"]/ul')
    for card in cards: print [[tema.text for tema in card.getchildren()]]
    temas_de_interesse = pagina.xpath('//article[@class="card"]/ul/li/text()')
    '''