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
        from complejos import Complex
        dis = b**2 -4*a*c
        if dis > 0 or dis ==0:
             root1 = (-b + np.sqrt(dis) )/2*a
             root2 = (-b - np.sqrt(dis))/2*a
        else:
            root1 = Complex((-b)/(2*a), np.sqrt(abs(dis) )/2*a)
            root2 = Complex((-b)/(2*a), np.sqrt(abs(dis) )/2*a)
           
            
        return [root1, root2]



#debemos agregar una función de verificación de la excatitud de la clase 

def test_Quadratic():
    from sympy import (symbols, lambdify, sqrt)
    x1, x2, f, a, b, c, x= symbols('x1 x2 f a b c x ')
    f = a*x**2 + b*x + c
    x1= (-b + sqrt(-4*a*c + b**2))/(2*a)
    x2 = (-b - sqrt(-4*a*c + b**2))/(2*a)
    t = lambdify([x,a, b,c], f)
    x_1 = lambdify([a, b, c], x1)
    root_1_exact = x_1(a = 1, b = 4, c = 4)
    x_2 = lambdify([a, b, c], x2)
    root_2_exact= x_2(a = 1, b = 4, c = 4)
    f_exact_value= t(x = 2, a = 1, b= 4, c = 4)
    f_computed = Quadratic(a = 1, b= 4, c= 4)
    f_computed_value = f_computed.value(x =2)
    computed_roots = f_computed.roots()
    root1_computed = computed_roots[0]
    root2_computed = computed_roots[1]
    diff = abs(f_exact_value - f_computed_value)
    diff2 = abs(root_1_exact - root1_computed)
    diff3 = abs(root_2_exact - root2_computed)
    tol = 1E-7
    assert diff < tol,'bug en la clase Quadratic, diff = %s' % diff
    assert diff2 < tol, 'bug en la clase Quadratic, diff2 = %s' % diff2
    assert diff3 < tol, 'bug en la clase Quadratic, diff3 = %s' % diff3
    
    
    
#     #revisar función test para varias verificaciones 
f_1 = Quadratic(a=10, b=3, c= 2)
m = f_1.value(x =2)
print(m)
n_2 = f_1.table(0, 100, 50)
print(n_2)
print(f_1.roots())

test_Quadratic()


        