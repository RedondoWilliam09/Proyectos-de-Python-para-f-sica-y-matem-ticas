# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 22:22:35 2021

@author: william

Clases para vectores en el plano

-_________________________________________________________
"""

class Vec2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return self.x*other.x + self.y*other.y
    
    
    def __abs__(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
    
    def __eq__(self, other):
        # return self.x == other.x and self.y == other.y 
        
        
        # #para el operador de igualdad dos cantidades pueden ser iguales pero solo 
        # en aproxmación dado que las componentes x y y son datos de punto flotante, 
        # por lo que necesitamos de una aproximación con error pequeño, una mejor implementación 
        # del método __eq__ es:
            
        import numpy
        return numpy.allclose(self.x, other.x) and \
            numpy.allclose(self.y, other.y)
            
        
    
    
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    
    def __ne__(self, other):
        return not self.__eq__(other) #reutiliza __eq__
    
    
    
# implementando la clase

u = Vec2D(0, 1)
v = Vec2D(1, 0)
w = Vec2D(1, 1)

a = u + v
print(a)

a==w
print(a==w)

a = u - v
print(a)
a = u*v
print(a)
print(abs(u))
print(u==v)
print(u != v)




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    