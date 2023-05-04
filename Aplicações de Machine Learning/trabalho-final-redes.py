# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:39:53 2023

@author: Lucas Marques
"""

import matplotlib.pyplot as plt
import numpy as np
import random

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# ENTRADAS
X = [      
      # Principais estados
         [0, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 1, 0, 0],
         [1, 0, 1, 0],
         [1, 0, 0, 1],
         
         
         # Outros casos
         
         # 0 x x x
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1],
         [0, 1, 1, 0],
         [0, 1, 1, 1],
         [0, 0, 1, 1],
         
         # 1 x x x 
         [1, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 0, 0, 1],
         [1, 0, 1, 1],
         [1, 1, 0, 1]
         
         
         
                  
     ]

# SAÍDAS
y1 = [ [0, 0, 0, 0],
       [0, 0, 0, 1],
       [1, 0, 0, 1],
       [1, 1, 0, 1],
       [1, 1 ,1, 1],
       
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       
       # Supondo comportamento de erro com chuveiro em stand by
       [0, 0, 0, 1],
       [0, 0, 0, 1],
       [0, 0, 0, 1],
       [0, 0, 0, 1],
       [0, 0, 0, 1] ]

clf1 = MLPClassifier(solver='lbfgs',activation='logistic', alpha=1e-5,hidden_layer_sizes=(450, 450), random_state=1)

clf1.fit(X, y1)




# TESTE
T=      [1, 0, 0, 0]

# TESTANDO
print("TESTANDO REDE: ")
print(clf1.predict([T]))
