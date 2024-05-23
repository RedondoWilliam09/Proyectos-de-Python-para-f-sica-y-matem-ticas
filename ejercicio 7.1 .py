# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 15:11:22 2022

@author: william
"""

# 7.1. construye una función de clase 

class F(object):
    """función exponencial con atributos de datos a y w """
    
    def __init__(self, a, w):
        self.a = a
        self.w = w
    
    def value(self, x):
        a, w = self.a, self.w
        import numpy as np
        return np.exp(-a*x)*np.sin(w*x)

f =F(a = 1.0, w = 0.1)
import numpy as np
print(f.value(x=np.pi))
print(f.a)
f.a = 2
print(f.value(x = np.pi))
 