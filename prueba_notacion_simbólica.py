# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 07:54:07 2022

@author: william
"""

from sympy import *

x, y, z = symbols("x y z")
expr = cos(x) + 1
print(expr.subs(x,y))
print(expr.subs(x,0))

expr = sin(2*x) + cos(2*x)
print(expand_trig(expr))
print(expr.subs(sin(2*x), 2*sin(x)*cos(x)))




# g , f, a, b, c, x= symbols('g f a b c x ')
# f = a*x**2 + b*x + c

# -b + sqrt( b**2  + (-4)*a*c  
# g = (-b + sqrt( b**2  + (-4)*a*c  ))/2*a
             
# # x2 = (-b - sqrt(-4*a*c + b**2))/(2*a)
# j = lambdify([x,a, b,c], f)
# f = j(x = 2, a = 1, b = 2, c = 9)
# print(f)


# d = lambdify([a, b, c], g)
# f = d(a = 1, b = 10, c = 9 )
# print(f)

c = solveset(Eq(x**2 + 2*x + 9), x)
print(c)
print(type(c))

