# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 18:41:56 2023

@author: Lucas Marques
"""
###### AULA DE APLICAÇÕES DE MACHINE LEARNING
#bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import read_csv
from pandas import set_option
import csv

#matplotlib: biblioteca para visualização de dados
#numpy: biblioteca para manipulação e análise de dados
#pandas: biblioteca para manipulação e análise de dados
#csv: classe para manipulação de dados em arquivos .csv/.txt

#ler dados do arquivo padrao.txt
Padrao = []
print("******************")
print("EFETUANDO A LEITURA DOS DADOS DO AQUIVO PADRÃO")

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\Aula3-correlacao\arquivoPadrao.txt"

#efetuar a abertura do arquivo para leitura
#ARQUIVO método para acesso aos dados no arquivo
with open(path, 'r', newline='') as ARQUIVO:
    #efetuar leitura dos dados no arquivo
    d = csv.reader(ARQUIVO)
    #converter vetor em uma lista - não necessario
    dd = list(d)
    #converter os valores lidos em um numero float
    for i in range(0, len(dd)):
        p = float(dd[i][0])
        Padrao.append(p)
        
#plotar dados
plt.plot( Padrao, 'b')
plt.title("SINAL DO ARQUIVO PADRÃO")
plt.xlabel("AMOSTRA [s]")
plt.ylabel("AMPLITUDE")
plt.show()

Dados4 = []
print("******************")
print("EFETUANDO A LEITURA DOS DADOS DO AQUIVO DADOS4")

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\Aula3-correlacao\arquivoDados4.txt"

#efetuar a abertura do arquivo para leitura
#ARQUIVO método para acesso aos dados no arquivo
with open(path, 'r', newline='') as ARQUIVO:
    #efetuar leitura dos dados no arquivo
    d = csv.reader(ARQUIVO)
    #converter vetor em uma lista - não necessario
    dd = list(d)
    #converter os valores lidos em um numero float
    for i in range(0, len(dd)):
        p = float(dd[i][0])
        Dados4.append(p)
        
#plotar dados
plt.plot( Dados4, 'g')
plt.title("SINAL DO ARQUIVO DADOS4")
plt.xlabel("AMOSTRA [s]")
plt.ylabel("AMPLITUDE")
plt.show()

#O método .corr utiliza o conceito de DataFrame para efetuar as 
#funções matemáticas implementadas.
#A variável (tabela) auxDFauxDF conterá os dados dos dois arquivos, 
#organizados em colunas.
#Utilizando o método disponível em PANDAS: pd.DataFrame(), os dados da 
#tabela auxDFauxDF serão convertidos em um DataFrame.
#A correlação é calculada pelo método .corr(method = 'pearson')
#implementado no objeto DataFrameDataFrame

#definir DataFrame com os valores lidos para aplicar correlacao
auxDF = []
DataFrame = []

# z variável auxiliar para montagem do dataframe
auxDF += [(float(float(Padrao[i])), float(Dados4[i])) for i in range(0, len(Padrao))]

#montagem
DataFrame = pd.DataFrame(auxDF, columns=['PADRAO', 'DADOS4'])

#calcular a correlação
correlacao = DataFrame.corr(method='pearson')
print("\nCoRRELAÇÃO TEMPORAL:")
print(correlacao)
print("\nDADOS ESTATÍSTICOS BÁSICOS - TEMPORAL")
print("NÚMERO DE AMOSTRAS/CAMPOS: ", DataFrame.shape)
print(DataFrame.describe())
