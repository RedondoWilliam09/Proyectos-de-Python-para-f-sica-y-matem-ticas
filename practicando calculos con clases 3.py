# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 08:51:24 2021

@author: william
"""

import numpy as np

import matplotlib.pyplot as plt

x= np.linspace(-4,4,41)

def h(x):
    return (1/np.sqrt(2*np.pi))*np.exp((-x**2)/2)

print(h(x))

plt.plot(x,h(x))
plt.title('función de distribución ')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.legend('función de distribución')

print(h(x))  #lista de elementos


