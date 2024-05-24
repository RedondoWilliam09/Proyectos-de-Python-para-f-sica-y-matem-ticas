# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 20:00:10 2021

@author: william
"""
# construyendo clases para números complejos 

class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        
        # return Complex(self.real + other.real,
        #                self.imag + other.imag)
    
        # podríamos mejorar  el método add de la siguiente manera..
        
        # if isinstance(other, (float, int)):
        #     return Complex(self.real + other, self.imag)
        # else:
        #     return Complex(self.real + other.real,
        #                    self.imag + other.imag)
        
        # una tercera implementación va de la forma...
        
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not (hasattr(other, 'real') and \
                  hasattr(other, 'imag')):
            raise TypeError('other must have real and imag attr.')
        
        return Complex(self.real + other.real,
                       self.imag + other.imag)
    
        
    
    
    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)
    
    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.real)
    
    def __div__(self, other):
            sr, si, ol, oi = self.real, self.imag, \
            other.real, other.imag #forma corta 
            
            r = float((ol)**2 + (oi)**2)
            return Complex((sr*ol + si*oi)/r, (si*ol - sr*oi)/r)
    
    def __abs__(self):
        from math import sqrt
        return sqrt(self.real**2 + self.imag**2)
    
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return 'Complex(%g +  %g*i)' % (self.real, self.imag)
    
    def __repr__(self):
        return 'Complex' + str(self)
    
    def __pow__(self, power):
        raise NotImplementedError\
            ('self**power is not yet impl. for Complex')
            
u = Complex(2,-1)
v = Complex(1)
d = Complex(4)

w = u + v
print(u)
print(w)

print(w != u)

print(u*v)
print(w + 4)

q = d - w
print(q)
print(d)

w = u + 4.5
print(w)

# w = 4.5 + u #me genera error 



# Python tuinen propiedades de escritura dinámica que nos dice 
# que por ejemplo los argumentos de funciones pueden cambiar durante la ejecución d un prgrama

#inspeccionando instancias 

class A(object):
    """Aclass for demo porpuses"""
    
    def __init__(self, value):
        self.v = value
    
    def dump(self):
        print(self.__dict__)

a = A([1,2])

a.dump()
print(dir(a))# regresa los nombre de todos los métodos y varables de un objeto 

print(a.__doc__)
print(a.__module__)

#vamos a intentar agregar nuevas variables a una instancia existente 

a.myvar = 10
a.dump()
print(dir(a))

b = A(-1)
b.dump()
print(dir(b))


        


















        