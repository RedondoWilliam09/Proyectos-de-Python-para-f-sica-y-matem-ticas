# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 10:52:43 2022

@author: william
"""



class Intervalmath(object):
    
    def __init__(self, lower, upper):
        self.lo = float(lower)
        self.up =float(upper)
    
    def __add__(self, other):
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return Intervalmath(a + c, b + d)
    
    def __sub__(self, other):
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return Intervalmath(a - c, b - d)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = Intervalmath(other, other)
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return Intervalmath(min(a*c, a*d, b*c, b*d), max(a*c, a*d, b*c, b*d)) 
    
    def __truediv__(self, other):
        
        a, b, c, d = self.lo, self.up, other.lo, other.up
        # el intervalo [c,d] no puede contener cero
        if c*d <= 0:
            raise ValueError\
                ('Interval %s no puede ser denomiador dado que '\
                 'este contiene cero' % other)
        
        
        return Intervalmath(min(a/c, a/d, b/c, b/d), max(a/c, a/d, b/c, b/d))
    
    def __str__(self):
        return '[%g, %g]' % (self.lo, self.up)
    
    #cuando intentamos multiplicar un objeto intervalmath con un objeto flotante, la
    #clase dará error, en cambio, podemos convertir
    #el objeto flotante en un intervalo con los mismo límites inferior y superior
    
    #la forma de aplicación de los métodos especiales no siempre es conmutativa, por ello necesitamos agregar métod demás 
    #para complemetar la función de un método 
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            other = Intervalmath(other, other)
        return other*self
    
    # también podemos implementar un método parat la potencia de un intervalo tal que..
    
    def __pow__(self, exponent):
        if isinstance(exponent, int):
            p = 1
            if exponent > 0:
                for i in range(exponent):
                    p = p*self
            elif exponent < 0:
                for i in range(-exponent):
                    p = p*self
                p = 1/p
            else: #exponente == 0
                p = Intervalmath(1,1)
            
            return p
        
        else:
            raise TypeError('El exponente debe ser entero')
    
    
    # podemos elegir convertir el intervalo en un flotante o iont, sacando el punto medio del intervalo 
    
    def __float__(self):
        return 0.5*(self.lo + self.up)
    
    def __repr__(self):
        return '%s(%g, %g)' % \
            (self.__clas__.__name__, self.lo, self.up)


    
    

    


# una implementación de las clase va de la forma 

I = Intervalmath 
a = I(-3, -2)
b = I(4, 5)
expr = 'a + b', 'a - b', 'a*b', 
for e in expr:
    print('%s = ' % e, eval(e))

print(a/b)
#revisar como utilizar el operador de división 


a = Intervalmath(5, 7)
print(float(a))

# una implementación completa de la clase va de la forma...


g = 9.81
y_0  = I(0.99, 1.01)  #2% de incertidumbre
Tm = 0.45  #media de T
T = I(Tm*0.95, Tm*1.05) #10% de incertidumbre 

print(T)
g = 2*y_0/T**(2)
print(g)
 
#podemos calcular con el valor medio 

T = float(T)
print(T)
y_0 = 1
g = 2*y_0/T**(2)
print('%2f' % g)

# podemos utilizar la misma  clase para estimar el volumen de una esfera 

Rm = 6
R = I(Rm*0.9, Rm*1.1)
from numpy import pi
V = (4/3)*pi*R**3
print(V)
print(float(V))
#podemos hacer el calculo del mismo volumen pero solo utilizando el valor medio del radio 
R = float(R)
V = (4/3)*pi*R**3
print(V)

     
        
        
        
        
        
        
        
        
        
        
        
        