# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 09:25:38 2022

@author: william

Implementando clases para números complejos 

__________________________________________________________________________
"""


# una clase para numeros complejos va de la forma...


class Complex(object):
    def __init__(self, real, imag = 0.0):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag, self.imag*other.real + self.real*other.imag)
    
    def __div__(self, other):
        sr, si, ol, oi = self.real, self.imag, \
            other.real, other.imag # forma corta 
        
        r = float(ol**2 + oi**2)
        return Complex((sr*ol+si*oi)/r, (si*ol - sr*oi)/r)
    
    def __abs__(self):
        from math import sqrt
        return sqrt(self.real**2 + self.imag**2)
    
    def __neg__(self): #define -c (c es un complejo)
        
        return Complex(-self.real, -self.imag)
    
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag
    
    def __ne__(self, other):
        
        return not self.__eq__(other)
    
    def __str__(self):
        return '(%g, %g)' % (self.real, self.imag)
    
    def __repr__(self):
        return 'Complex' + str(self)
    
    def __pow__(self, power):
        raise NotImplementedError\
            ('self**power is not yet impl. for Complex')

        
u = Complex(2, -1)
v = Complex(1)

w = u + v
print(w)

print(w != u)
print(u*v)

print(w + 4)
print(w - 4)



    
    
    
    
    
    
    
    
    
    
    
    
    


    
    
        
        