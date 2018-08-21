import csv
from datetime import datetime
linhas = []
with open('BBC-Results.csv', 'rb') as csvfile:
    r = csv.reader(csvfile, delimiter=' ', quotechar='|') 
    linha_count = 0
    for linha in r:
        if linha_count < 100:
            linhas.append(linha)
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
                    print data.date().strftime('%d/%m/%Y') + ' ' + ','.join(str(a) for a in resto)
                    linha_count += 1
                except Exception as e:
                    #print e
                    pass
        else:
            break
