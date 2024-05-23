# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 09:27:18 2022

@author: william
"""

from math import *
from sympy import * 

x_1, f, a, b, c, x= symbols(' x_1 f a b c x ')
f = a*x**2 + b*x + c
x1= (-b + sqrt(-4*a*c + b**2))/(2*a)
x2 = (-b - sqrt(-4*a*c + b**2))/(2*a)
t = lambdify([x,a, b,c], f)
d = t(x = 2, a = 1, b= 6, c = 9)
print(d)

x_1 = lambdify([a, b, c], x1)
x__1 = x_1(a = 1, b = 6, c = 9)
print(x__1)




# root2_exact_N = lambdify([a, b, c], x2)
# x2_exact = root2_exact_N(a = 1, b = 6, c = 9)
# f_2 = Quadratic(a = 1, b= 6, c= 9)
# exact_value= c(x = 2, a = 1, b= 6, c = 9)
# computed_value = f_2.value(x =2)
# computed_roots = f_2.roots()
# root1_computed = computed_roots[0]
# root2_computed = computed_roots[1]    