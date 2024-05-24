# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 11:16:05 2021

@author: william

de objetos de matemáticas a objetos en python.

________________________________________
"""

class Circle(object):
    def __init__(self, x0, y0, R):
        self.x0, self.y0, self.R = x0, y0, R
    
    def area(self):
        from numpy import pi
        return pi*self.R**2
    
    def circunference(self):
        from numpy import pi
        return 2*pi*self.R


#Usando la clase tenemos la siguiente sintáxis...

c = Circle(2, -1, R=5)

print('un circulo con radio %g a (%g, %g) tiene área %g m^2'  %  \
      (c.R, c.x0, c.y0, c.area() ))

    
    
#Podemos crear una función de verificación para verificar si la clase Circle es correcta 

def test_Circle():
    R= 2.5
    c = Circle(7.4, -8.1, R)
    
    from math import pi
    expect_area = pi*R**2
    computed_area = c.area()
    diff = abs(expect_area - computed_area)
    tol = 1E-14
    assert diff < tol, 'bug in circle.area, diff %s' % diff
    
    
    expect_circunference = 2*pi*R
    computed_circunference = c.circunference()
    diff = abs(expect_circunference - computed_circunference)
    assert diff < tol, 'bug in Circle.circunference, diff = %s' % diff
    
    
    
   











