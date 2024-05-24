# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 21:45:02 2021

@author: william
"""

#MÉTODOS ESPECIALES 


#diferenciación automática 

def f(x,y):
    return x**3 + y**((4/5)*x**3)

from sympy import symbols, diff
x, y= symbols('x y')
dfdx= diff(f(x,y),x)
dfdy= diff(f(x,y),y)
print('las derivadas simbólicas son:', dfdx, dfdy)

#clase para una derivada numética 

class Derivative(object):
    def __init__(self, f, h= 1E-5):
        self.f = f
        self.h = float(h)
    
    def __call__(self, x):
        f,h = self.f, self.h  #para construir de la forma corta 
        return (f(x + h) - f(x))/h
    

#vamos a derivar dos funciones 

from math import sin, cos, pi

df = Derivative(sin)
x= pi
print(df(x))

df2 = Derivative(cos)
print(df2(x))
print(cos(x))

def g(t):
    return t**3

dg = Derivative(g)
t= 1
print('el valor de la derivada es: ', dg(1))


#verificación 

# ###############################################################--------método de Newton
def Newton(f, x, dfdx, epsilon=1.0E-7, N=100, store=False):
    f_value = f(x)
    n = 0
    if store: info = [(x, f_value)]
    while abs(f_value) > epsilon and n <= N:
        dfdx_value = float(dfdx(x))
        if abs(dfdx_value) < 1E-14:
            raise ValueError("Newton: f'(%g)=%g" % (x, dfdx_value))

        x = x - f_value/dfdx_value

        n += 1
        f_value = f(x)
        if store: info.append((x, f_value))
    if store:
        return print(x, info)
    
    else:
        return print(x, n, f_value)

# -------------------------------------------------------------------

def test_Derivative():
    #la fórmula es exacta para funciones lineales, independientemente de h 
    f = lambda x: a*x + b
    a = 3.5; b= 8
    dfdx= Derivative(f, h= 0.5)
    diff= abs(dfdx(4.5) - a)
    assert diff < 1E-14, 'bug in class Derivative,  Diff = %s' % diff 
    # print(diff)

print(test_Derivative(), 'es el eeror respecto de la función lineal en la función de prueba')


#APLICACIÓN, MÉTODO DE NEWTON 

# from classes import Derivative



def f(x):
    return 100000*(x - 0.9)**2 * (x - 1.1)**3
    
df = Derivative(f)

Newton(f, 1.01, df, epsilon = 1E-5)
print('por el método de Newton')



#derivando usando notación simbólica de Sympy

class Derivative_sympy(object):
    def __init__(self, f):
        from sympy import Symbol, diff, lambdify
        x = Symbol('x')
        sympy_f = f(x)
        sympy_dfdx = diff(sympy_f, x)
        self.__call__ = lambdify([x], sympy_dfdx)
       
def test_Derivative_sympy():
    def g(t):
        return t**3
    dg = Derivative_sympy(g)
    t = 2
    exact = 3*t**2
    computed = dg(t)
    tol = 1E-14
    assert abs(exact - computed) < tol

    def h(y):
        return exp(-y)*sin(2*y)
    from sympy import exp, sin
    dh = Derivative_sympy(h)
    from math import pi, cos
    y = pi
    exact = (-1)*exp(-y)*sin(2*y) + exp(-y)*2*cos(2*y)
    computed = dh(y)
    assert abs(exact - computed) < tol

















