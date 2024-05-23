# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 11:10:56 2021

@author: william
"""

#función definida a trozos
from math import *
from matplotlib.pyplot import *
import numpy as np


def H(x):
    return   ( 0 if x < 0 else 1)
    
 #proando con pocos puntos:

x=np.linspace(-10,10,1000)

def  H_loop(x):
    r= np.zeros(len(x))
    for i in range(len(x)):
        r[i]= H(x[i])
    return r
y= H_loop(x)


plot(x, y)
axis=(-2, 2, -2, 2)
show()

#segunda función de prueba:
    
# función de sombrero 
def N(x):
    if x < 0:
        return 0.0
    elif 0 <= x < 1:
        return x
    elif 1 <= x < 2:
        return 2 - x
    elif x >= 2:
        return 0.0

def  H_lop(x):
    r= np.zeros(len(x))
    for i in range(len(x)):
        r[i]= N(x[i])
    return r

z= H_lop(x)

plot(x,z)
show()

#función que varia rápidamente

def f(x):
    return np.sin(1/x)

x1= np.linspace(-1, 1, 10)
x2= np.linspace(-1, 1, 1000)


plot(x1, f(x1))
show() 
plot(x1, f(x2))
axis([-1, 1, -1, 1])









