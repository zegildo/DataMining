from lxml import html 
from lxml import etree 
import pandas as pd

if __name__ == "__main__":
    
    arquivo = open('/home/jrdesktop/MT10/mulheres_palestrantes.htm').read()
    pagina = etree.HTML(arquivo)
    
    nomes = pagina.xpath('//article[@class="card"]/h3/text()')
    localizacoes = pagina.xpath('//article[@class="card"]/div/p[@class="location"]/text()')
    fotos = pagina.xpath('//article[@class="card"]/img/@src')

    participantes = []
    
    for nome,foto,localizacao in zip(fotos,nomes,localizacoes):
        participante = {'nome':nome, 'foto':foto, 'localizacao':localizacao}
        participantes.append(participante)
        

    
    csv_file = pd.DataFrame(participantes)
    csv_file.to_csv('participantes.csv', sep=',', encoding='utf-8')
    