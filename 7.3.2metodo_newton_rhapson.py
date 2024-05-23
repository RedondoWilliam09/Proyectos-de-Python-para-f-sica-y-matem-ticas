# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 23:27:01 2022

@author: william
"""

def Newton(f, x, dfdx, epsilon = 1.0E-7, N = 100, store = False):
    f_value = f(x)
    n = 0
    if store : info = [(x, f_value)]
    while abs(f_value) > epsilon and n <= N:
        dfdx_value = float(dfdx(x))
        if abs(dfdx_value) < 1E-14:
            raise ValueError("Newton: f'(%g) = %g" % (x, dfdx_value))
        
        x = x - f_value/dfdx_value
        
        n += 1
        f_value = f(x)
        if store: info.append((x, f_value))
    if store:
        return x, info
    else:
        return x, n, f_value

# podemos empezar con una función y su derivada 

from math import sin, cos, pi, exp


def g(x):
    return exp(-0.1*x**2)*sin(pi/2*x)

def dg(x):
    return -2*0.1*x*exp(-0.1*x**float(2))*sin(pi/2*x) + \
        (pi/2)*exp(-0.1*x**float(2))*cos(pi/2*x)

def l(x):
    return x**2 -3
def dl(x):
    return  2*x

def p(x):
    return x**3 + 1
def dp(x):
    return  3*x**2

        
x0 = input('inserte el valor de x0= ')
x0= float(x0)
x, info = Newton(g, x0, dg, store = True)

print('root :', x)
for i in range(len(info)):
    print('iteración %3d: f(%g) = %g' % \
          (i, info[i][0], info[i][1]))
    
x, info = Newton(l, x0, dl, store = True)
print('root :', x)
for i in range(len(info)):
    print('iteración %3d: f(%g) = %g' % \
          (i, info[i][0], info[i][1]))
        

x, info = Newton(p, x0, dp, store = True)
print('root :', x)
for i in range(len(info)):
    print('iteración %3d: f(%g) = %g' % \
          (i, info[i][0], info[i][1]))
        
def H(x):
    return 100000*(x - 0.9)**2*(x - 1.1)**3

class Derivative(object):
    def __init__(self, f, h= 1E-5):
        self.f = f
        self.h = float(h)
    
    def __call__(self, x):
        f,h = self.f, self.h  #para construir de la forma corta 
        return (f(x + h) - f(x))/h
    

dH = Derivative(H)
print(Newton(H, x0, dH, epsilon = 1E-5))




# (Revisar código)


    
    
    