
# Investigação de dados

## DataSet: _Não comparecimento as consultas médicas_

Esta base de dados possui informações de 100.000 consultas médicas no Brasil e está focado na questão de buscar compreender se o paciente irá ou não comparecer a consulta. As características sobre os pacientes são descritas em cada linha.

<li>**ScheduledDay:** informa o dia em que o paciente marcou sua consulta.
<li>**Neighborhood:** indica a localização do hospital.
<li>**Scholarship:** indica se o paciente está ou não envolvido com o programa Bolsa Família.
Tenha cuidado ao interpretar a última coluna. **'No'** significa que o paciente compareceu a consulta previamente agendada. Por outro lado, **'Yes'** signifca que ele não compareceu.

## Table of Contents

<ul>
<li><a href="#intro">Introduction</a></li>
<li><a href="#wrangling">Data Wrangling</a></li>
<li><a href="#eda">Exploratory Data Analysis</a></li>
<li><a href="#conclusions">Conclusions</a></li>
</ul>

## Perguntas

**1)** Quem mais falta as consultas homens ou mulheres?<br>
**2)** Qual a proporção de pacientes que não comparecem às consultas?<br>
**3)** Qual a distribuição da idade de pacientes que não comparecem às consultas?<br>
**4)** Há alguma relação entre doença e não comparecimento às consultas?<br>
**5)** Qual a cidade com maior número de não comparecimentos?<br>
**6)** Qual é o mês, dia da semana e dia do mês com maior número de não comparecimentos?<br>
**7)** Há alguma correlação entre a participação no programa social Bolsa Família e os comparecimentos?

## Carregar os dados:



```python
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
#dtype={'AppointmentDay': str}
df = pd.read_csv('noshowappointments-kagglev2-may-2016.csv');

df.head()
#df.dtypes
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PatientId</th>
      <th>AppointmentID</th>
      <th>Gender</th>
      <th>ScheduledDay</th>
      <th>AppointmentDay</th>
      <th>Age</th>
      <th>Neighbourhood</th>
      <th>Scholarship</th>
      <th>Hipertension</th>
      <th>Diabetes</th>
      <th>Alcoholism</th>
      <th>Handcap</th>
      <th>SMS_received</th>
      <th>No-show</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.987250e+13</td>
      <td>5642903</td>
      <td>F</td>
      <td>2016-04-29T18:38:08Z</td>
      <td>2016-04-29T00:00:00Z</td>
      <td>62</td>
      <td>JARDIM DA PENHA</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5.589978e+14</td>
      <td>5642503</td>
      <td>M</td>
      <td>2016-04-29T16:08:27Z</td>
      <td>2016-04-29T00:00:00Z</td>
      <td>56</td>
      <td>JARDIM DA PENHA</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.262962e+12</td>
      <td>5642549</td>
      <td>F</td>
      <td>2016-04-29T16:19:04Z</td>
      <td>2016-04-29T00:00:00Z</td>
      <td>62</td>
      <td>MATA DA PRAIA</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8.679512e+11</td>
      <td>5642828</td>
      <td>F</td>
      <td>2016-04-29T17:29:31Z</td>
      <td>2016-04-29T00:00:00Z</td>
      <td>8</td>
      <td>PONTAL DE CAMBURI</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.841186e+12</td>
      <td>5642494</td>
      <td>F</td>
      <td>2016-04-29T16:07:23Z</td>
      <td>2016-04-29T00:00:00Z</td>
      <td>56</td>
      <td>JARDIM DA PENHA</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
</div>



# **1)** Quem mais falta as consultas homens ou mulheres?


```python
df.groupby(["Gender", "No-show"]).size()


```




    Gender  No-show
    F       No         57246
            Yes        14594
    M       No         30962
            Yes         7725
    dtype: int64



Conclusão: Com um total de 14.594(mulheres) e 7725(homens) podemos afirmar que as mulheres faltam mais que os homens ás consultas médicas. 




# **2.** Qual a proporção de pacientes que não comparecem às consultas? 



```python
df.groupby('No-show')['AppointmentID'].nunique().plot(kind='bar')


```




    <matplotlib.axes._subplots.AxesSubplot at 0x7effe07d4610>




![png](output_9_1.png)


# 3.Qual a distribuição da idade de pacientes que não comparecem às consultas?


```python
distribuicao = df[df['No-show'] == 'Yes']


```


```python
distribuicao[['No-show','Age']].hist(bins=120,alpha=0.5,color='#FF005E')
plt.savefig('nomeDaFigura.png')    

```


![png](output_12_0.png)


Conclusão: Podemos perceber, que o maior numero de faltas concentram-se em bebês, em seus primeiros meses de vida.

# **4)** Há alguma relação entre doença e não comparecimento às consultas?

Podemos agrupar os dados levando em consideração as doenças e as faltas, o 1 representa que existe determinada doença, e o 0 é que não, primeiro agruparemos as pessoas que tenham pelos menos uma das doenças definidas na base de dados:


```python
hipertensos = df.loc[df['Hipertension'] == 1, ['No-show', 'Hipertension']]
hipertensosCont = hipertensos.loc[hipertensos['No-show'] == 'Yes', ['Hipertension']].count()

diabetes = df.loc[df['Diabetes'] == 1, ['No-show', 'Diabetes']]
diabetesCont = diabetes.loc[diabetes['No-show'] == 'Yes', ['Diabetes']].count()
alcoolismo = df.loc[df['Alcoholism'] == 1, ['No-show', 'Alcoholism']]
alcoolismoCont= alcoolismo.loc[alcoolismo['No-show'] == 'Yes', ['Alcoholism']].count()

```

Em seguida, contamos a quantidade de vezes que as doenças são detectada nas consultas não realizadas 


```python

labels = ['Hipertensos', 'Diabetes', 'Alcoolismo']
sizes = [hipertensosCont,diabetesCont , alcoolismoCont]
fig1,ax1= plt.subplots()
ax1.pie(sizes,labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()
plt.savefig('pizza.png')    

    
    
```


![png](output_18_0.png)



    <matplotlib.figure.Figure at 0x7effdf9e3ad0>


Conclusão:Podemos perceber, que os hipertensos são os que tem maiores probabalidade de faltar  

# **5)** Qual a cidade com maior número de não comparecimentos?<br>



```python
cidade= distribuicao.groupby('Neighbourhood').size()
cidade.loc[ cidade['Neighbourhood'].idxmax()]
df_grouped = df.groupby('Neighbourhood').size().reset_index(name='Missing appointments')

#pd.value_counts(distribuicao['Neighbourhood'].values.flatten())
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-54-e2e8386fa29e> in <module>()
          1 cidade= distribuicao.groupby('Neighbourhood').size()
    ----> 2 cidade.loc[ cidade['Neighbourhood'].idxmax()]
          3 
          4 #pd.value_counts(distribuicao['Neighbourhood'].values.flatten())


    /usr/local/lib/python2.7/dist-packages/pandas/core/series.pyc in __getitem__(self, key)
        866         key = com.apply_if_callable(key, self)
        867         try:
    --> 868             result = self.index.get_value(self, key)
        869 
        870             if not is_scalar(result):


    /usr/local/lib/python2.7/dist-packages/pandas/core/indexes/base.pyc in get_value(self, series, key)
       4386                     raise InvalidIndexError(key)
       4387                 else:
    -> 4388                     raise e1
       4389             except Exception:  # pragma: no cover
       4390                 raise e1


    KeyError: 'Neighbourhood'


Como podemos ver, o hospital com maior numero de não comparecimentos é o das proximidades do  JARDIM CAMBURI com 1465 não comparecimentos, o JARDIM CAMBURI, está localizado na cidade de Vitória-ES

# **6)** Qual é o mês, dia da semana e dia do mês com maior número de não comparecimentos?


```python
Primeiro, iremos transformar a coluna AppointmentDay para o tipo datetime  
```


```python


distribuicao['AppointmentDay']=pd.to_datetime(distribuicao.AppointmentDay)




```

    /home/vectro26/.local/lib/python2.7/site-packages/ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      This is separate from the ipykernel package so we can avoid doing imports until


Agora, agrupamos o numero de consultas por mês


```python
df.groupby(distribuicao['AppointmentDay'].dt.month).size()

```




    AppointmentDay
    4.0      633
    5.0    16804
    6.0     4882
    dtype: int64



Como podemos perceber, o mês 5(MAIO) é o que dispoẽ de maior quantidade de tuplas agrupadas, 
ou seja, ele é o mês com maior numero de faltas. Em seguida, agrupamos os dias do mês 5 
para podemos obter os dados de faltas por dia da semana


```python
dias = distribuicao[distribuicao.AppointmentDay.dt.month==5]
pd.value_counts(dias.AppointmentDay.dt.dayofweek.values.flatten())


```




    1    4336
    0    3817
    2    3507
    4    2599
    3    2536
    5       9
    dtype: int64



Como podemos observar, o dia da semana  que ocorre maior numero de faltas, é a terça-feira
com 4336 faltas


```python
pd.value_counts(dias.AppointmentDay.dt.day.values.flatten())

```




    16    1049
    9     1019
    10     992
    4      973
    17     935
    13     905
    20     899
    19     892
    18     890
    30     888
    11     885
    2      861
    12     837
    3      831
    24     811
    5      807
    6      795
    31     767
    25     759
    14       9
    dtype: int64



Podemos observar,que no dia 16 é o dia que ocorre o maior numero de faltas, com 1049 faltas ocorridas no dia.

# **7)** Há alguma correlação entre a participação no programa social Bolsa Família e os comparecimentos?


```python
df.groupby(["Scholarship", "No-show"]).size()


```




    Scholarship  No-show
    0            No         79925
                 Yes        19741
    1            No          8283
                 Yes         2578
    dtype: int64




```python
Conclusão: Os participantes do Bolsa Famíla correspondem a 10861, os mesmo em sua grande 
maioria, no total de 8283 não faltam as consultas, o que correspondem a 76% das consultas
realizadas com os participantes do programa.

```
