# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 08:07:24 2021

@author: william
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


def f(x,t):
    return np.exp(-(x - 3*t)**2)*np.sin(3*np.pi*(x - t))

x=t=np.linspace(-5, 5, 21)

x,t= np.meshgrid(x,t)  #devuelve las matrices de coordenadas de lo vectores de coordenadas 
z = f(x,t)

fig= plt.figure()
ax= Axes3D(fig)
fig.add_axes(ax)
ax.plot_surface(x,t,z,rstride=1, cstride=1, cmap=cm.viridis )  #los demás parámetros son para determinar la resolución y el color de la suerfice
plt.title('superficie $e^{-(x-3t)^2}sin(3 pi (x-t))$')
plt.show()

x= np.linspace(-4, 4, 100)

plt.plot(x,f(x,t=0))
plt.title('paquete de onda')
plt.show()