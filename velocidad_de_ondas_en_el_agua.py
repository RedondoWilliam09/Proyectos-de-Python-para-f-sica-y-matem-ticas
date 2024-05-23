# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 08:24:35 2021

@author: william
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


def cc(lamnda,g,rho,h,s):
    return np.sqrt((g*lamnda/(2*np.pi))*(1 + s*((4*(np.pi)**2)/(rho*g*(lamnda)**2)))*np.tanh((2*np.pi*h)/(lamnda)))

lamnda=np.linspace(0.001,0.1 , 1000)
g=9.81
s= 7.9
rho= 1000
h= 50


plt.plot(lamnda,cc(lamnda,g, rho, h,s))
plt.title('velocidad de las ondas superficiales en el agua')
plt.xlabel('longitud de onda ')
plt.ylabel('velocidad de la onda')

plt.show()