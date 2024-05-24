# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:24:10 2022

@author: william
"""

#podemos construir una clase pra integrar una función en una variable 
#utilizando la regla del trapecio para integración numérica 

#la clase toma la siguiente forma 

def trapezoidal(f, a, x, n):
            h = (x - a)/float(n)
            I = 0.5*f(a)
            for i in range(1,n):
                I += f(a + i*h)
            I +=0.5*f(x)
            I *= h
            return I
        
class Integral(object):
    def __init__(self, f, a, n= 100):
        self.f, self.a, self.n = f, a, n
    
    def __call__(self, x):
        def trapezoidal(f, a, x, n):
            h = (x - a)/float(n)
            I = 0.5*f(a)
            for i in range(1,n):
                I += f(a + i*h)
            I +=0.5*f(x)
            I *= h
            return I
        
        return trapezoidal(self.f, self.a, x, self.n)
    

from math import sin, pi
G = Integral(sin, 0, 200)
value = G(2*pi)
print(value)
value = trapezoidal(sin, 0, 2*pi, 200)
print(value)


# podemos hacer una verificación vía cálculo simbólico 

import sympy as sp
x = sp.Symbol('x')
f_expr = sp.cos(x) + 5*x
print(f_expr)
F_expr = sp.integrate(f_expr, x)
print(F_expr)
F = sp.lambdify([x], F_expr) 
print(F(0))
print(F(1))


#ahora podemos escribir nuestra funcióin test de la forma 

def test_Integral():
    #la regla trapezoidal es exacta para funciones lineales 
    import sympy as sp
    x = sp.Symbol('x')
    f_expr = 2*x + 5
    f = sp.lambdify([x], f_expr)
    #calculamos la integral exacta en notación simbólica 
    F_expr = sp.integrate(f_expr, x)
    F = sp.lambdify([x], F_expr)
    
    a = 2
    x = 6
    exact = F(x)- F(a)
    T = Integral(f, a, n = 4)
    computed = T(x)
    diff = abs(exact - computed)
    tol = 1E-15
    assert diff < tol, 'bug en la clase integral, diff=%s'  % diff
    
#d34, 440.