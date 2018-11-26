from lxml import html 
from lxml import etree 

if __name__ == "__main__":
    
    """
        http://insideoutproject.xyz/mulheres-palestrantes/
    """
    arquivo = open('mulheres_palestrantes.html').read()
    pagina = etree.HTML(arquivo)
    
    nomes = pagina.xpath('//article[@class="card"]/h3/text()')
    fotos = pagina.xpath('//article[@class="card"]/img/@src')
    localizacoes = pagina.xpath('//article[@class="card"]/div/p[@class="location"]/text()')
    temas_de_interesses = pagina.xpath('//article[@class="card"]/ul/li/text()')
    participantes = []
    
    for nome,foto,localizacao,tema_de_interesse in zip(nomes,fotos,localizacoes,temas_de_interesses):
         with open('bancodedados.sql', 'a') as file:  # Use file to refer to the file object
        
          file.write("INSERT INTO PALESTRANTES VALUES('" +nome+"','"+foto+"','"+localizacao+"','"+tema_de_interesse+"');")
          file.write("\n") 
          file.close()
    

