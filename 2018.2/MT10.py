from lxml import html 
from lxml import etree 
import pandas as pd

if __name__ == "__main__":
    
    """
        http://insideoutproject.xyz/mulheres-palestrantes/
    """
    arquivo = open('mulheres_palestrantes.htm', mode='r', encoding="utf-8").read()
    pagina = etree.HTML(arquivo)
    
    nomes = pagina.xpath('//article[@class="card"]/h3/text()')
    temas_de_interesse = pagina.xpath('//article[@class="card"]/ul/li/text()')
    participantes = []
    
    for nome,temas_de_interesses in zip(nomes,temas_de_interesse):
        participante = ((nome,temas_de_interesses))

        participantes.append(participante)

    csv_file = pd.DataFrame(participantes, columns=['Nome', 'TEMAS DE INTERESSES'])

    csv_file.to_csv('Lista_Participantes.csv', sep=',', encoding='utf-16')
         
    #convertido em sql no:http://convertcsv.com/csv-to-sql.htm
