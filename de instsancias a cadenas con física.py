# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 12:25:39 2022

@author: william

Entendiendo arquitectura de código con problemas de física

_______________________________________
"""

class Y:
    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81
    
    def value(self, t):
        return self.v0*t - 0.5*self.g*t**2
    
    #podemos agragar un metodo especial para imprimir una cadena 
    
    def __str__(self):
        return 'v0*t - 0.5*g*t**2; v0 = %g' % self.v0

#una clase mejorada podemos contruirla solo con mètodos especiales 

class Y2(object):
    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81
    
    def __call__(self, t):
        return self.v0*t - 0.5*self.g*t**2
    
    def __str__(self):
        return 'v0*t - 0.5*g*t**2; v0 = %s' % self.v0
    

#poniendo la clase en acción tenemos..

y = Y2(1.5)  #contruyo la instancia y, y agrego el valor de v0 en el constructor 
print(y(0.2))  #evaluo el método especial de llamda __call__ dentro de la clse Y2, 
                #con los valores almacenados en la instancia y

print(y) # solo imprime lo que está contenido dentro de la instancia 








