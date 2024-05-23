# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 06:19:13 2021

@author: william
"""

#nota: A^2 y A^2 son computacionalmente diferentes, sin embargo, la 
#primera se refiere al producto de dos matrices, mientras que la segunda se refiere a elevar los 
#elementos de una matriz al cuadrado

#   MATRICES DIDIMENSIONALES Y FUNCIONES DE DOS VARIABLES 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


def f(x,y):
    return np.sin(np.sqrt(x**2 + y**2)) + np.sin(x)

x=y=np.linspace(-5, 5, 21)

x,y= np.meshgrid(x,y)  #devuelve las matrices de coordenadas de lo vectores de coordenadas 
z = f(x,y)

fig= plt.figure()
ax= Axes3D(fig)
fig.add_axes(ax)
ax.plot_surface(x,y,z,rstride=1, cstride=1, cmap=cm.viridis )  #los demás parámetros son para determinar la resolución y el color de la suerfice
plt.title('superficie $sin((x^2 + y^2)^{1/2}) + sin(x)$')
plt.show()


print('-------------------')

x1= np.array([1,2,3], float)
x2= np.matrix(x1)  #me devuelve un vector fila 
print(x2)

x3= np.mat(x2).transpose() #me genera el transpuesto o vector columna 
print(x3)

print(x3*x1) # es una matriz
print(x1*x3) # es un escalar

s = x3*x1
print(4*s) #multiplicación de una matriz por un escalar
print(type(x3))
print(isinstance(x3, np.matrix))

A= np.eye(3) #me genera una matriz identidad de 3x3
print(A)
A= np.mat(A).transpose() #matriz transpuesta
print(A)

y2= x2*A   #producto vector-matriz
print(y2)

y3= A*x3  #producto matriz-vector
print(y3)

#el operador de multiplicación entre objetos ndarray es bastante diferente:
    
#print(A*x1) #las matrices no está alineadas

A= (np.zeros(9) + 1).reshape(3,3) #en una forma 3x3
print(A)
print(A*x1)  # es el equivalente a hacer # [A[0,:]*x1, A[1,:]*x1, A[2,:]*x1]

B= A + 1

print(B)
print(A*B)  #producto baado en elementos

A=np.mat(A); B= np.mat(B)
print(A*B)     #prodcuto matriz-matriz


#vectorizacion de una función constante 


def ff(x):
    return 2

#pero esta matriz devuelve un flotante
# para que devuelva un array hacemos:
     
def fv(x):
    return np.zeros(x.shape, x.dtype) +2


#una forma mas optimizada sería..

def fff(x):
    if isinstance(x, (float, int)):
        return 2
    elif isinstance(x, np.ndarray):
        return np.zeros(x.shape, x.dtype) + 2
    else:
        raise TypeError\
            ('x debe ser entero, flotante o array, no %s' % type(x))

print(fff(x= 20))

s=np.linspace(-2,2, 100)

plt.plot(s, fff(s)) # la funcion queda directamente vectorizada
plt.title('funcion f(x)= 2 vectorizada')
plt.xlabel('x')
plt.ylabel('fff(x)')
plt.show()



#forma compacta de la función linspace

w= np.r_[-5:5:11j]  # es lomismo que tener np.linspace(-5,5,11)
print(w)

#manipulación de formas de matrices 


a= np.r_[-1:1:6j]
print(a)
print(a.shape)
print(a.size)

a.shape= (2,3)    #forma de la matriz
a= a.reshape(2,3)  #forma de la matriz
print(a)

print(len(a))  #nuemro de filas

a.shape= (a.size,)  #regresar a la forma de linspace
print(a)
      
 #  IMPLEMENTACIÓN ESCALAR 
#ecuación de la recta ectorizada=

def axpy_loop_newr(a,x,y,r):
    r = np.zeros_like(x)
    for i in range(r.size):
        r[i]= a*x[i] + y[i]
        return r

#podemos hacer también=

def axpy_loop(a,x,y,r):
    for i in range(r.size):
        r[i]= a*x[i] + y[i]
    return r    #dejamos que la matriz la proporcione el usuario 

#la implementación vectorizada va como..
#from memory_profiler import *
from memory_profiler import profile

@profile
def axpy1(a,x,y):
    r= a*x + y
    return r



























