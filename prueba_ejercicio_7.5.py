# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 12:00:29 2022

@author: william
"""

from ejercicio_7_5 import Quadratic, test_Quadratic

f_1 = Quadratic(a=20, b=3, c= 2)
m = f_1.value(x =2)
print(m)
n_2 = f_1.table(0, 100, 50)
print(n_2)
print(f_1.roots())

n =test_Quadratic()
print(n)

from ejercicio_7_6 import Line, test_Line

linea = Line((4,3),(1,2)) 
x_1 = linea.value(10)
print(x_1)

test_Line()
