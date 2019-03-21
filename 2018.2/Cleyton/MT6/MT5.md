
# MT5: Visualização de dados de amigos do facebook através de boxplot 


```python
%matplotlib inline
import pandas as pd
df_face = pd.read_csv('FacebookFrends.csv');
df_face
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
      <th>Timestamp</th>
      <th>How many</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>02/01/2013 16:59:06</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>02/01/2013 15:20:50</td>
      <td>69</td>
    </tr>
    <tr>
      <th>2</th>
      <td>02/01/2013 16:16:51</td>
      <td>123</td>
    </tr>
    <tr>
      <th>3</th>
      <td>02/01/2013 18:14:04</td>
      <td>137</td>
    </tr>
    <tr>
      <th>4</th>
      <td>02/01/2013 20:04:27</td>
      <td>174</td>
    </tr>
    <tr>
      <th>5</th>
      <td>02/01/2013 16:59:09</td>
      <td>240</td>
    </tr>
    <tr>
      <th>6</th>
      <td>02/01/2013 15:19:48</td>
      <td>241</td>
    </tr>
    <tr>
      <th>7</th>
      <td>02/01/2013 16:35:58</td>
      <td>256</td>
    </tr>
    <tr>
      <th>8</th>
      <td>02/01/2013 16:28:28</td>
      <td>258</td>
    </tr>
    <tr>
      <th>9</th>
      <td>02/01/2013 23:18:28</td>
      <td>322</td>
    </tr>
    <tr>
      <th>10</th>
      <td>02/01/2013 16:17:02</td>
      <td>366</td>
    </tr>
    <tr>
      <th>11</th>
      <td>02/01/2013 16:30:23</td>
      <td>376</td>
    </tr>
    <tr>
      <th>12</th>
      <td>02/01/2013 15:26:34</td>
      <td>408</td>
    </tr>
    <tr>
      <th>13</th>
      <td>02/01/2013 17:56:35</td>
      <td>479</td>
    </tr>
    <tr>
      <th>14</th>
      <td>02/01/2013 15:56:00</td>
      <td>555</td>
    </tr>
    <tr>
      <th>15</th>
      <td>02/01/2013 15:19:35</td>
      <td>589</td>
    </tr>
    <tr>
      <th>16</th>
      <td>03/01/2013 10:20:51</td>
      <td>600</td>
    </tr>
    <tr>
      <th>17</th>
      <td>02/01/2013 15:39:28</td>
      <td>777</td>
    </tr>
    <tr>
      <th>18</th>
      <td>02/01/2013 15:21:24</td>
      <td>784</td>
    </tr>
    <tr>
      <th>19</th>
      <td>02/01/2013 15:46:07</td>
      <td>822</td>
    </tr>
    <tr>
      <th>20</th>
      <td>02/01/2013 16:53:47</td>
      <td>850</td>
    </tr>
    <tr>
      <th>21</th>
      <td>02/01/2013 16:23:35</td>
      <td>863</td>
    </tr>
    <tr>
      <th>22</th>
      <td>02/01/2013 15:20:15</td>
      <td>1116</td>
    </tr>
    <tr>
      <th>23</th>
      <td>02/01/2013 16:24:46</td>
      <td>1143</td>
    </tr>
    <tr>
      <th>24</th>
      <td>02/01/2013 15:21:11</td>
      <td>1214</td>
    </tr>
    <tr>
      <th>25</th>
      <td>07/01/2013 18:15:32</td>
      <td>1250</td>
    </tr>
    <tr>
      <th>26</th>
      <td>02/01/2013 15:26:57</td>
      <td>1776</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_face.plot.box()

```




    <matplotlib.axes._subplots.AxesSubplot at 0x129aee04a58>




![png](output_2_1.png)



```python

```
