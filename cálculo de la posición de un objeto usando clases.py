# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:36:23 2021

@author: william

implementación de una clase con métodos para emular una función como método
#de clase para el cálculo de posiciones

___________________________________

"""


class V(object):
    def __init__(self, beta, mu0, n, R):
        self.beta, self.mu0, self.n, self.R = beta, mu0, n, R
    
    def value(self, r):
        beta, mu0, n, R= self.beta, self.mu0, self.n, self.R
        n=float(n) #asegurar la dicisión por flotantes 
        v= (beta/(2.0*mu0))**(1/n)*(n/(n+1))*\
            (R**(1+1/n) - r**(1+ 1/n))
        return v

c = V(1,2,4,20)
print(c.value(2), 'es el valor de la variable v en el método value()')


#implemenatciones de clases de fucniones alternativas 

#implementacion alternativa de la clase Y

class Y2(object):
    def value(self,t, v0= None):
        if v0 is not None:
            self.v0= v0
        g= 9.81
        return self.v0*t - 0.5*g*t**2


# ¿si no hay constructor, cómo se crea la instancia?

# python crea un constructor vacío, esto nos eprmite escribir


y=Y2()
# pero aun no tiene TRIBUTO

# LLAMNDO

y.value(0.1, 5)
print(y.v0)
v= y.value(0.2)
print(v)
























