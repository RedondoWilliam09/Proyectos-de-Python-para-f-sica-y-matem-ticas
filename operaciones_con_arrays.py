# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 12:01:26 2021

@author: william
"""

import numpy as np

x= np.array([1, 2, 3.5])
# a=x
# a[-1]= 3
# a[0]= 2
# print(a)
# print(x)

# #5.6.2. haciendo copias de un array

# a= x.copy()
# a[-1]= 9
# print(a)
# print(x)

#aritmética in situ 

#haciendo eficiente el cálculo con matrices 

#a +=b es equivalente a decir a= a+b
#pero es mas eficiente usar a +=b dado que no crea nuevas matrices solo agrega elementos a la matriz existente 

#podemos tenr un cálculo de matriz compuesta 

# a= (3*x**4 + 2*x + 4)/(x + 1)

#podemos hacer lo siguiente 

a=x.copy() #tenemos que tener primero definido x dado que a en este caso es una copia DE X
a **= 4
a *= 3
a += 2*x
a += 4
a /= x + 1
print(a)
print(x)
#ESTO ES MUY IMPORTANTE EN LA EFICIENCIA DE CÓDIGO 

print('---')
print(x)

v=x
v += x  # es multiplicar a x por si misma 

print('el valor de v es :', v)

#asignación de matrices 

a= np.linspace(1,8,8)
print('a= ',a)
a[[1,6,7]]=10
print(a)
a[range(2,8,3)]= -2
print(a)

#podemos usar matrices boleanas para generar un conunto de índices

print(a[a<0])
a[a<0]= a.max()
print(a)

print(type(a))  #tipo de elemento 

print(isinstance(a, np.ndarray)) #vericiar si a es un array 
print(isinstance(a, (float,int)))# verificar si a es un ino o un floAT 

a= np.linspace(-1, 1, 6)

print(a)
a.shape
print(a.shape) #elementos en la matriz

a.shape= (2,3)
a= a.reshape(2,3)
print(a.shape)
print(a)

#MATRICES DE ORFDEN SUPERTIOR 
    


















