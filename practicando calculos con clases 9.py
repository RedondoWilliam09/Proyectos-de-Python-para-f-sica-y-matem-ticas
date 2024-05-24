# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 10:03:26 2022

@author: william
"""


#CLASE PARA UNA LINEA RECTA 

#contruye unaclase en la cual elconstriuctor tome dos puntos  
# p1 y p2 (2 tuplas o dos listas ) como entradas, la linea pasarà a 
# travès de esto
# dos puntos, calcula un mètodo value para evaluar la linea en el puto x. 
# Tambien construye una funciòn test.Line() para verificar la implementaciòn

class Line(object):
    def __init__(self, p1, p2):
        self.p1, self.p2  = p1, p2
    
    def value(self, x):
        x1, y1, x2, y2 = self.p1[0], self.p1[1], self.p2[0], self.p2[1]
        if x2 != x1:
            m = (y2 - y1)/(x2-x1)
            c = -m*x1 + y1
            y = m*x + c
            return y
        else:
            print('los valores de x1 y x2 no pueden ser iguales dado que se  llega a una ideterminaciòn en  el càlculo de la apendiente ')
        
    
linea = Line((4,3),(1,2)) 
x_1 = linea.value(10)
print(x_1)
  
def test_Line():
    from sympy import symbols, lambdify
    y, x, y1, y2, x1, x2, m, c, M, C = symbols('y x y1 y2 x1 x2 m c M C')
    m = (y2 - y1)/(x2 - x1)
    c = -M*x1 + y1
    y = M*x + C
    t  = lambdify([y2, y1, x2, x1], m)
    f = lambdify([M, x1, y1], c)
    z = lambdify([M, x, C], y)
    m_ = t(2, 3, 1, 4)
    c_ = f(m_, 4, 3)
    y_exact = z(m_, 10, c_)
    lin= Line((4,3),(1,2)) 
    y_computed = lin.value(10)
    tol = 1E-8
    diff = abs(y_exact - y_computed)
    assert diff < tol, 'bug en la clase line, diff = %s' % diff
    
test_Line()

    
   
    
           