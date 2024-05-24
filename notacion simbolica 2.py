# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 21:50:05 2022

@author: william


Notacición simbólica con python 2.

_________


"""

from sympy import (symbols, diff, integrate, Rational, lambdify, sin, exp, cos, latex, simplify, expand)

t, v0, g = symbols('t v0 g')
y = v0*t - Rational(1,2)*g*t**2
dydt = diff(y,t)
print(dydt)

h = sin(t)*exp(t) + 1
dydh= diff(h,t)
print(dydh)
iH= integrate(h,t)
print(iH)

print('la aceleración es :', diff(y, t, t), 'que es el equivalente de la segunda derivada')

y2 = integrate(dydt, t)
print(y2)
v = lambdify([t, v0, g], dydt)
print(v(t = 0, v0 = 5, g = 9.81))

z = lambdify([t, v0, g], y)
print(z(t = 0, v0 = 5, g = 9.81))

from sympy import solve
roots = solve(y, t)
print(roots)


# aproximando una función por polinomios de Taylor, y haciendolo para dos funciones tenmos...


f = exp(t)
print(f.series(t, 0, 10)) #lo evalua en t y lo expande de 0 a 10

f = exp(sin(t))
print('el valor de la expansión para esta función es: ', \
      f.series(t, 0, 8))

print(latex(f.series(t, 0, 7)))

#también hay herrmainetas para expandir y simplificar expresiones 

x, y = symbols('x y')
f = -sin(x)*sin(y) + cos(x)*cos(y)
print(simplify(f))


print(expand(sin(x + y), trig = True))














