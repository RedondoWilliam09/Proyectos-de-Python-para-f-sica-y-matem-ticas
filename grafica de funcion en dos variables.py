# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 07:33:37 2021

@author: william
"""

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

