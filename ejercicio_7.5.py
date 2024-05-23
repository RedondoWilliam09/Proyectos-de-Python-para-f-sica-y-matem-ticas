# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 05:06:17 2022

@author: william
"""

#una clase para funciones cuadráticas 

class Quadratic(object):
    def __init__(self, a=0, b= 0, c= 0):
        self.a, self.b, self.c = a, b, c
    
    def value(self, x):
        a, b, c = self.a, self.b, self.c
        return a*x**2 + b*x + c
    
    def table(self, L, R, n):
        import numpy as np
        x = np.linspace(L,R,n)
        f = self.value(x)
        for i in range(n):
            print([x[i], f[i]])
    def roots(self):
        a, b, c = self.a, self.b, self.c
        import numpy as np
        root1 = (-b + np.sqrt(b**2 -4*a*c)/2*a)
        root2 = (-b - np.sqrt(b**2 -4*a*c)/2*a)
        print(root1, root2)

f_1 = Quadratic(a=1, b=3, c= 2)
m = f_1.value(x =2)
print(m)
n_2 = f_1.table(0, 100, 50)
print(n_2)
print(f_1.roots())


        