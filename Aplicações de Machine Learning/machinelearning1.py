# CARGA DE BIBLIOTECAS
import matplotlib.pyplot as plt
import numpy as np
import random

# https://scikit-learn.org/stable/
from sklearn import linear_model
from sklearn.metrics import r2_score

import pandas as pd
from pandas import read_csv
from pandas import set_option
import time as tm

# LEITURA DADOS# LEITURA DADOS
dados=pd.read_csv("D:\FuelConsumptionCo2.csv")
# RETORNA UM CERTO NUMERO DE LINHAS – MINIMO 5
dados.head()

# SEPARANDO DOIS CAMPOS PARA ANALISE
dados=dados[["ENGINESIZE","CO2EMISSIONS"]]
# IMPRIMIR OS DADOS
print(dados)

# PLOTANDO A CURVA DOS PARAMETROS: ENGINESIZE x CO2EMISSIONS
plt.scatter(dados["ENGINESIZE"],dados["CO2EMISSIONS"],color=
"green")
plt.xlabel("Volume do Motor")
plt.ylabel("EMISSAO DE CO2")
plt.show()

# BASE DE DADOS: TREINO - UTILIZAREMOS 08% DOS DADOS TABELADOS
#SEPARAR 80% DA BASE DE DADOS
treino=dados[:(int((len(dados)*0.8)))] 

# LEITURA DADOS# LEITURA DADOS
dados=pd.read_csv("D:\FuelConsumptionCo2.csv")
read_csv("D:\FuelConsumptionCo2.csv") 

'''Comando PANDAS para efetuar a leitura de dados de 
um arquivo .CSV
retorna um DataFrame com os dados (separados por 
vírgula) do arquivo/BD'''

# RETORNA UM CERTO NUMERO DE LINHAS # RETORNA UM CERTO NUMERO DE LINHAS –– MINIMO MINIMO 55
dados.head()

'''Comando PANDAS retorna um certo número de linhas do DataFrame – mínimo 5
.head(20) retorna as 20 primeiras linhas'''

'''MatplotlibMatplotlib Application Interfaces (Application Interfaces (APIsAPIs)    )  
  .matplotlib.  É uma API que implementa vários métodos, como por exemplo, o pyplot que 
  implementa várias funções de compatibilidade com o 
MathLab'''
import matplotlib.pyplot as plt #plt é um alias para matplotlib.pyplot
# pyplotpyplot..scatterscatter(x[],y[],(x[],y[],colorcolor=cor)    =cor)    efetua a plotagem de dados não ordenados em “x”
plt.scatter(dados["ENGINESIZE"],dados["CO2EMISSIONS"],color="green")
# pyplotpyplot..plotplot(x(x[],y[],[],y[],colorcolor=cor)    =cor)    efetua a plotagem de dados x[],y[]
plt.plot(dados["ENGINESIZE"],dados["CO2EMISSIONS"],color="green")
# # pyplotpyplot..xlabelxlabel(“rótulo para o eixo X”)(“rótulo para o eixo X”)
# # pyplotpyplot..yylabellabel(“rótulo para o (“rótulo para o eixo Y”)eixo Y”)
plt.xlabel("Volume do Motor")
plt.ylabel("EMISSAO DE CO2")
plt.ylabel("EMISSAO DE CO2")
# # pyplotpyplot.show()    .show()    efetua a apresentação do gráfico ou figura
plt.show()

# "regressao" OBJETO PARA Regressao Linear
regressao=linear_model.LinearRegression()
# SEPARANDO OS CAMPOS
treino_x=np.array(treino[["ENGINESIZE"]])
treino_y=np.array(treino[["CO2EMISSIONS"]])
# Determinar os parametros da Regressao Linear
# retorna:   regressao.coef_ coeficiente de inclinacao da curva de Regressao Linear
#            regressao.intercept_ valor de interceptacao no eixo y para x_[0]
regressao.fit(treino_x,treino_y)
# DETERMINAR O PARAMETRO R^2 # DETERMINAR O PARAMETRO R^2 
SCORE=regressao.score(treino_x,treino_y)
# PRINT PARAMETROS DA REGRESSAO LINEAR# PRINT PARAMETROS DA REGRESSAO LINEAR
print("***** TREINO DATA")
print("Coeficiente de Regressão =",regressao.coef_)
print("Interceptação = ",regressao.intercept_)
print("Fator de Regresssão",SCORE)

# linear_modellinear_model..LinearRegressionLinearRegression()   ()   define objeto para o modelo de Regressão Linear
regressao=linear_model.LinearRegression()
# SEPARANDO OS CAMPOS
treino_x=np.array(treino[["ENGINESIZE"]])
treino_y=np.array(treino[["CO2EMISSIONS"]])
# ..fitfit Ajustar o modelo de Regressao Linear
# retorna:   regressao.coef_ coeficiente de inclinacao da curva de Regressao Linear
#            regressao.intercept_ valor de interceptacao no eixo y para x_[0]
regressao.fit(treino_x,treino_y)
'''..scorescore(X[],y[])(X[],y[]) DETERMINAR O PARAMETRO R^2 
valor entre 0 e 1
0 indica muita variação do dados em relação à reta - Regressão Linear
1 indica pouca variação do dados em relação à reta - Regressão Linear   '''
SCORE=regressao.score(treino_x,treino_y)