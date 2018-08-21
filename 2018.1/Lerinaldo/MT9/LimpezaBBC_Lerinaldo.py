import csv
from datetime import datetime
import os
import pandas as pd
 
def meucsv(path):
    retorno = None
    if os.path.isfile(path):
        try:
            retorno = []
            linhas = []
            with open(path, 'rb') as csvfile:
                r = csv.reader(csvfile, delimiter=' ', quotechar='|')
                linha_count = 0
                for linha in r:
                    if linha_count < 100:
                        linhas.append(linha)
                        #print linhas
                        if len(linha)==2:
                            try:
                                data = datetime.strptime(linha[0], '%d/%m/%Y')
                                resto_dividido = linha[1].split(',')
                                resto = []
                                for i in range(len(resto_dividido)):
                                    da_vez = resto_dividido[i]
                                    if len(da_vez)>0:
                                        if len(da_vez)>4:
                                            resto.append(da_vez)
                                        else:
                                            try:
                                                valor = int(da_vez)
                                            except Exception as e:
                                                #print e
                                                pass
                                            else:
                                                resto.append(valor)
                                data = {"data": data.date().strftime('%d/%m/%Y'), "resto": ','.join(str(a) for a in resto)}
                                retorno.append(data)
                                linha_count += 1
                            except Exception as e:
                                #print e
                                pass
                    else:
                        break
        except Exception as e:
            #print e
            pass
    return retorno
 
 
 
path = 'BBC-Results.csv'
a = meucsv(path)
csv_file = pd.DataFrame(a)
csv_file.to_csv('teste2.csv', sep='\t', encoding='utf-8')
