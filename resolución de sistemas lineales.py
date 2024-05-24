# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 08:46:53 2021

@author: william
"""

#sistemas lineales 

import numpy as np

A= np.array([[1,2],[-2,2.5]])

x = np.array([-1,1], dtype=float)  #eliges una solución x para el sistema
b= np.dot(A,x)
h= np.linalg.solve(A,b)
print(h)   # que es efectivamente la solución x


#operaciones con filas y comnas y eliminación gaussiana 


import sympy as sym

A= sym.Matrix([[2,0],[0,5]])

print(A**(-1))   #inversa de A
print(A.inv())    #inversa de A
print(A.det())   #determinante de A
print(A.transpose())   #A transpuesta de A

print(A.eigenvals())  #autovalores de A   me imprime un diccionario
e= list(A.eigenvals().keys())  #pasar los autovalores a una lista 
print(e)

print('los autovectores son: ', A.eigenvects()) #da una lista con los valores propios y los ectores propios


v = [[t[2][0][i,0] for i in range(t[2][0].shape[0])] for t in A.eigenvects()]
print('v es :', v)