import  pandas as  pdpd
import  matplotlib.pyplot as plt


#Analise Descritiva dos Orçamentos da Ufersa campus Angicos 2017



x = ['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV']
y = [273026.44,197963.83,237754.81,248757.67,265345.23,211406.82,218744.72,319725.87,275540.09,273191.89,220214.01]

plt.plot(x, y, color='g')
plt.title('Relatorio de Despesas 2017')
plt.xlabel('Meses')
plt.ylabel('Capital usado')

plt.show()

#Questão 1: No orçamento da UFERSA campus Angicos qual o mês teve maior indice dos gastos em 2017?

#R: No mês de agosto houve um aumento significativo nas categorias: energia, bolsas/auxilios e motoristas com esse
#aumento pode-se afirmar que o respectivo mês está no topo dos maiores orçamentos gasto na ufersa campus Angicos.

x = ['Energia','Água','Correios','Bolsas\ne Auxílios','Limpeza','Portaria',
     'Vigilância','Água\nMineral','Motorista','Reprografia','Inscrições','Aluno\nEvento','Dispensas']
y = [42899.09,2200.66,21.5,105580,46404.04,20570.24,18667.74,602,76002.5,478.05,0,6300,0]

plt.bar(x,y, label= 'Barsl', color='g')
plt.xlabel('Categoria')
plt.ylabel('Capital usado')
plt.title('Relatorio de Despesas de Agosto de 2017')
plt.rcParams['figure.figsize']=(14,0)

plt.show()

#Questão 2: No mês de agosto pode-se notar um aumento em algumas categorias
# Por qual motivo os gastos com motoristas subiram?

#Pode-se afirmar que o aumento no orçamento correspondente aos motoristas dá-se ao numero
# de eventos externos que necessitam de locomoção aumentou, consequentimente os gasto naquele mês tambem subiu.

#Questão 3: Por qual motivo no mês de agosto os gastos com bolsas/auxilios subiram?

#Teoricamente o aumento no orçamento da UFERSA correspondente a bolsas/auxilios em agosto
#dá-se por conta de uma nova cota de alunos concorrentes, a junção dessa nova cota com a cota ainda ativa gera
#um aumento no orçamento para o respectivo mês.

#Questão 4: Ainda no mês de agosto pode-se notar um aumento na categoria energia, um dos maiores do ano,
# Quais os motivos desse fenomeno?

#Aparentimente no respectivo mês houve eventos na instituição, com isso se fez necessário a utilização de alguns ambientes
#com maior frequencia, por exemplo: Auditório Central, o mesmo tem um alto consumo de energia pois necesseita de climatização
# uma boa iluminação e outros aparelhos eletronicos, o uso de laboratorios com maior frequencia tambem gera mais consumo
# de energia e entre outros.



gastosCom = ['Energia','Água','Correios','Bolsas e Auxílios','Limpeza','Vigilância','Água Mineral','Motorista']

qtdGasta = [19181.70, 5041.66, 38.66, 44500, 149748.98, 36887.62, 1083.60, 16482.12]
cores = ['c','m','brown','orange','r','b','black','gold']

plt.pie(qtdGasta, labels = gastosCom, colors = cores)
plt.title('Capital usado em Janeiro de 2017')
plt.xlabel('OBS: Valores zerados e minimos seriam irrelevantes para esse gráfico')
plt.rcParams['figure.figsize']=(7,7)

plt.show()

#Questão 5: No mês de janeiro pode-se notar um grande aumento nos setores de limpeza, vigilancia e com produtos como
#agua mineral. Por qual motivo isso ocorreu?

#Como não há registro de gastos em dezembro é correto afirmar que no mês de janeiro
# é calculado os gastos do mês de dezembro juntamente com o mês de janeiro por isso o aumento das dispesas
#nos setores e com água mineral.

#Questão 6: Na transição do mês de dezembro a janeiro tambem houve um aumento nos gastos com bolsas/auxilios
#por qual motivo isso acontece?

#Isso acontece da mesma forma que na questão 3 a diferença é que a validade das bolsas/auxilios se encerram em dezembro
# diminuindo temporariamente os gastos e em janeiro  um nova seleção é feita para os ingressantes com consequencia disso
# pode-se notar o aumento no mês de janeiro na categoria bolsas/auxilios.