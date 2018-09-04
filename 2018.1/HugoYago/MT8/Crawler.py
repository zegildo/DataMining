import requests
from lxml import html
import pandas as pd
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
            titulos_links = {"\33[1;32;mTitle ":titulo,"Link":link}
            lista_titulos_links.append(titulos_links)
    return lista_titulos_links
noticias = get_lista_noticias()
lista_titulos_links = lista_titulos_links(noticias)
csv_file = pd.DataFrame(lista_titulos_links)
csv_file.to_csv('title_link.csv', sep=',', encoding='utf-8')
#print (csv_file)