# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 09:46:25 2023

@author: Lucas Marques
"""

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

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\trabalho_final_correlacao\ecomercePadrao.txt"

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
        

DadosJaneiro = []
print("******************")
print("EFETUANDO A LEITURA DOS DADOS DO AQUIVO REFERENTE A JANEIRO")

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\trabalho_final_correlacao\ecomerceJaneiro.txt"

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
        DadosJaneiro.append(p)
        
        
DadosFevereiro = []
print("******************")
print("EFETUANDO A LEITURA DOS DADOS DO AQUIVO REFERENTE A FEVEREIRO")

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\trabalho_final_correlacao\ecomerceFevereiro.txt"

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
        DadosFevereiro.append(p)


DadosMarco = []
print("******************")
print("EFETUANDO A LEITURA DOS DADOS DO AQUIVO REFERENTE A MARCO")

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\trabalho_final_correlacao\ecomerceMarco.txt"

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
        DadosMarco.append(p)
        
        
DadosAbril = []
print("******************")
print("EFETUANDO A LEITURA DOS DADOS DO AQUIVO REFERENTE A ABRIL")

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\trabalho_final_correlacao\ecomerceAbril.txt"

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
        DadosAbril.append(p)



DadosMaio = []
print("******************")
print("EFETUANDO A LEITURA DOS DADOS DO AQUIVO REFERENTE A MAIO")

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\trabalho_final_correlacao\ecomerceMaio.txt"

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
        DadosMaio.append(p)
        
        
DadosJunho = []
print("******************")
print("EFETUANDO A LEITURA DOS DADOS DO AQUIVO REFERENTE A JUNHO")

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\trabalho_final_correlacao\ecomerceJunho.txt"

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
        DadosJunho.append(p)
        
DadosJulho = []
print("******************")
print("EFETUANDO A LEITURA DOS DADOS DO AQUIVO REFERENTE A JULHO")

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\trabalho_final_correlacao\ecomerceJulho.txt"

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
        DadosJulho.append(p)
        

DadosAgosto = []
print("******************")
print("EFETUANDO A LEITURA DOS DADOS DO AQUIVO REFERENTE A AGOSTO")

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\trabalho_final_correlacao\ecomerceAgosto.txt"

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
        DadosAgosto.append(p)
        
        

DadosSetembro = []
print("******************")
print("EFETUANDO A LEITURA DOS DADOS DO AQUIVO REFERENTE A SETEMBRO")

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\trabalho_final_correlacao\ecomerceSetembro.txt"

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
        DadosSetembro.append(p)
        
        

DadosOutubro = []
print("******************")
print("EFETUANDO A LEITURA DOS DADOS DO AQUIVO REFERENTE A OUTUBRO")

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\trabalho_final_correlacao\ecomerceOutubro.txt"

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
        DadosOutubro.append(p)
        
        
        
DadosNovembro = []
print("******************")
print("EFETUANDO A LEITURA DOS DADOS DO AQUIVO REFERENTE A NOVEMBRO")

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\trabalho_final_correlacao\ecomerceNovembro.txt"

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
        DadosNovembro.append(p)
        
        
        
DadosDezembro = []
print("******************")
print("EFETUANDO A LEITURA DOS DADOS DO AQUIVO REFERENTE A DEZEMBRO")

path = r"C:\Users\Lucas Marques\Documents\Especialização\Aplicações de Machine Learning\trabalho_final_correlacao\ecomerceDezembro.txt"

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
        DadosDezembro.append(p)



auxDF = []
DataFrame = []

# z variável auxiliar para montagem do dataframe
auxDF += [(float(float(Padrao[i])), float(DadosJaneiro[i]), float(DadosFevereiro[i]), float(DadosMarco[i]), float(DadosAbril[i]), float(DadosMaio[i]), float(DadosJunho[i]), float(DadosJulho[i]), float(DadosAgosto[i]), float(DadosSetembro[i]), float(DadosOutubro[i]), float(DadosNovembro[i]), float(DadosDezembro[i])) for i in range(0, len(Padrao))]

#montagem
DataFrame = pd.DataFrame(auxDF, columns=['PADRAO', 'JANEIRO', 'FEVEREIRO', 'MARCO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO'])

#calcular a correlação
correlacao = DataFrame.corr(method='pearson')
print("\nCoRRELAÇÃO TEMPORAL:")
print(correlacao)
print("\nDADOS ESTATÍSTICOS BÁSICOS - TEMPORAL")
print("NÚMERO DE AMOSTRAS/CAMPOS: ", DataFrame.shape)
print(DataFrame.describe())

