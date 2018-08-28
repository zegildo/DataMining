import requests
from lxml import html
import pandas as pd

def padroniza_titulo(titulo):
    return titulo.encode('latin-1').decode('utf-8')

def get_lista_noticias():
    URL = 'http://www.globo.com/'
    response = requests.get(URL)  
    body = html.fromstring(response.text)
    noticias = body.xpath('//a[contains(@class,"hui-highlight__link")]')
    return noticias

def lista_titulos_links(noticias):
    lista_titulos_links = []
    for noticia in noticias:
        if 'title' in noticia.attrib:
            titulo = padroniza_titulo(noticia.attrib['title'])
            link = noticia.attrib['href']
            lista_titulos_links.append((titulo, link))
    return lista_titulos_links

noticias = get_lista_noticias()
lista_titulos_links = lista_titulos_links(noticias)
csv_file = pd.DataFrame(lista_titulos_links, columns = ['Titulo', 'Link'])
print(csv_file)
csv_file.to_csv('saidasMT-8.csv')