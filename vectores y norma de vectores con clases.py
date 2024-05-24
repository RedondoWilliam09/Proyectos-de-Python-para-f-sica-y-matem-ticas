# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 08:55:17 2022

@author: william

Implementación de una clase para crear objetos tipo vectores en dos dimensiones.

__________________________________________________________________________
"""

# podemos implementar una clase para representar vectores en 2 dimensiones de la siguioente forma...


class Vect2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vect2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vect2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return self.x*other.x + self.y*other.y
    
    def __abs__(self):
        from math import sqrt
        return sqrt(self.x**2 + self.y**2)
    
    def __eq__(self, other):
        
        #return self.x == other.x and self.y == other.y
        
        #la operación anterior funciona correctamente, pero para evitar problemas de igualdad
        #dados los redondeos en los datos flotantes, es mejor utilizar la siguiente implementación..
        import numpy as np
        return np.allclose(self.x, other.x) and \
            np.allclose(self.y, other.y)
        
        
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    
    def __ne__(self, other):
        return not self.__eq__(other) #~reutiliza __eq__
    
# una utilidad de la clase para vectores va de la forma...

u = Vect2D(0,1)
v = Vect2D(1,0)
w = Vect2D(1,1)

a = u + v
print(a)

print(a== w)
a = u -v
print(a)

a = u*v
print(a)
print(abs(u))

print(u==v)
print(u != v)

 















    
    
    
    
    
    