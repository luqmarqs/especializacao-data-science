# -*- coding: utf-8 -*-
"""
Created on Thu May 19 19:56:04 2023

@author: AM
"""

import matplotlib.pyplot as plt
import numpy as np
import random

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# ENTRADAS
X = [      
          [1.,1.,1.,1.,
           1.,0.,0.,1.,
           1.,0.,0.,1.,
           1.,1.,1.,1.,
           1.,0.,0.,1.,
           1.,0.,0.,1.],
 
         [1.,0.,0.,1.,
          1.,0.,1.,0.,
          1.,1.,0.,0.,
          1.,1.,0.,0.,
          1.,0.,1.,0.,
          1.,0.,0.,1.],

         [1.,1.,1.,0., 
          1.,0.,0.,1.,
          1.,1.,1.,0.,
          1.,0.,0.,1.,
          1.,0.,0.,1.,
          1.,1.,1.,0.],
          
         [1.,1.,1.,1.,
          0.,1.,1.,0.,
          0.,1.,1.,0.,
          0.,1.,1.,0.,
          0.,1.,1.,0.,
          1.,1.,1.,1.],
         
         [1.,0.,0.,0.,
          0.,1.,0.,0.,
          0.,0.,1.,1.,
          0.,0.,1.,1.,
          0.,1.,0.,0.,
          1.,0.,0.,0.],
                  
     ]

# SAÍDAS
y1 = [ ['A'], ['K'], ['B'], ['I'], ['>'],]


clf1 = MLPClassifier(solver='lbfgs',activation='logistic', alpha=1e-5,hidden_layer_sizes=(450,450), random_state=1)

clf1.fit(X, y1)

# SAÍDA NUMÉRICA
y2 = [[1.,0.,0.,0.,0.], [0.,1.,0.,0.,0.],[0.,0.,1.,0.,0.], [0.,0.,0.,1.,0.], [0.,0.,0.,0.,1.]]
clf2 = MLPClassifier(solver='lbfgs',activation='logistic', alpha=1e-5,hidden_layer_sizes=(450,450), random_state=1)

clf2.fit(X, y2)


# TESTE
T=       [1.,0.,0.,1.,
          1.,0.,0.,1.,
          1.,1.,1.,0.,
          1.,1.,0.,0.,
          1.,0.,1.,0.,
          1.,0.,0.,1.]

# TESTANDO
print("TESTANDO REDE 1: ")
print(clf1.predict([T]))

# TESTANDO
print("TESTANDO REDE 2: ")
resultado=clf2.predict([T])
print(resultado)
for i in range(len(resultado[0])):
    print("PADRÃO ",i," - RESULTADO: ",resultado[0][i])



