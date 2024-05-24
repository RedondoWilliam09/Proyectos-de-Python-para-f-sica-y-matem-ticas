# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 07:51:47 2021

@author: william

operaciones comunes en algebra lineal con python

_______
"""

import numpy as np

A= np.array([[2,0],[0,5]],dtype= float)

print(A)

#para la inversa de la matriz tenemos:

B= np.linalg.inv(A)
print(B)
print(A*B)  # ME DA LA INDENTIDAD

#para el determinante de la matriz tenemos:
    

C=np.linalg.det(A)  
print(C)

#para autovalores y autovectores tenemos:

f= eig_values, eig_vectors = np.linalg.eig(A)
print(f)

#los autovectores se normalizan para tener unidades de longitud

#PROODUCTOS 

#usos de np.dot

a= np.array([4,0])
b=np.array([0,1])
print(np.dot(A,a))
print(np.dot(a,b))

c= np.array([[1,2],[3,4]])
f= np.array([[5,6],[7,8]])

print(c,f)
print(np.dot(c,f))
print(a)

k= np.ones((2,2)) #matriz de unos de 2x2
print(k)
print(np.dot(A,k))


#producto cruz entre vectores

v= np.array([[1,1,1]])
d= np.array([0,0,1])
print(np.cross(v,d))
 
#norma de vectores:
    
print(np.linalg.norm(v))

#para el ángulo entre vectores:

o= np.arccos((np.dot(v,d))/(np.linalg.norm(v)*np.linalg.norm(d)))

print(o)  #àngulo en radianes


#NORMAS

print(A)

print(np.linalg.norm(A))  #norma de frobenius, que es la raíz de la suma de los cuadrados de los elementos de matriz
print(np.sqrt(np.sum(A**2))) #norma de frobenius 
print('LA NORMA DE V ES= ' , np.linalg.norm(v)) #norma genérica para vectores

#transpuesta de una matriz
print('------')
print(A)
print(np.transpose(A))  #A ES UNA MATRIZ SIMÉTRICA
print(np.transpose(v))   #funciona con vectores pero respetando la sintaxis del array
print(np.transpose(v)*v)  #revisar la notacion del doc anterior

print('norma= ?', np.linalg.norm(v))
print(v)  

print(c)
print(np.transpose(c))

#suma y valores extremos 

print(np.sum(A)) #SUMA DE LOS ELELEMTOS DE LA ATRIZ

print(A.sum())

print(np.sum(A, axis= 0))   # suma sobre el índice 0 (filas)

print(np.sum(A, axis= 1))   # suma sobre el índice 0 (columnas)
print(c)

print(np.sum(c, axis= 0))   # suma sobre el índice 0 (filas)

print(np.sum(c, axis= 1))   # suma sobre el índice 0 (columnas)


#ALTERNATIVA DE TRANSPUESTA DE MATRIZ=

B= np.array([[1,2],[3,4]], dtype=float)
print(B)
print(B.T)#transpuesta de la matriz

#triangular inferor y triangular superior=

print(np.triu(B)) #superior 
print(np.tril(B)) #tringular inferior

#traza de una matriz 
print(np.trace(B))

#diagonal de una matriz







