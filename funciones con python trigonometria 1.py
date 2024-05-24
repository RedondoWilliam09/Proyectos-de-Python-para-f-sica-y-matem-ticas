# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 09:27:13 2021

@author: william


gráficas de funciones con python.

.............
"""

#función definida a trozos
from math import *
from matplotlib.pyplot import *
import numpy as np



def f(x):
    return np.sin(1.0/x)

x1= np.linspace(-1, 1, 10)
x2= np.linspace(-1, 1, 1000)


#plot(x1, f(x1))
#show()
plot(x2, f(x2))
#show()
axis([-1, 1, -1, 1])
title('funciones que varian rápidamente $sin(1/x)$')