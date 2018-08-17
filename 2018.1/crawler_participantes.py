#coding: utf-8

from lxml import html 
from lxml import etree 

if __name__ == "__main__":

    arquivo = open('/Users/zegildo/Desktop/UFERSA/Disciplinas/2017.2/MineracaoDeDados/DataMining-Projects/2018.1/mulheres_palestrantes.htm').read()
    pagina = etree.HTML(arquivo)
    
    nomes = pagina.xpath('//article[@class="card"]/h3/text()')
    fotos = pagina.xpath('//article[@class="card"]/img/@src')
    localizacoes = pagina.xpath('//article[@class="card"]/div/p[@class="location"]/text()')

    participantes = []
    
    for nome,foto,localizacao in zip(nomes,fotos,localizacoes):
        participante = {'nome':nome, 'foto':foto, 'localizacao':localizacao}
        participantes.append(participante)
    print participantes

    '''
    cards = pagina.xpath('//article[@class="card"]/ul')
    for card in cards: print [[tema.text for tema in card.getchildren()]]
    temas_de_interesse = pagina.xpath('//article[@class="card"]/ul/li/text()')
    '''
