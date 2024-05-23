# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 22:02:40 2021

@author: william
"""

class SpacePoint(object):
    counter = 0
    def __init__(self, x, y, z):
        self.p = (x,y,z)
        SpacePoint.counter += 1


p1 = SpacePoint(0, 0, 0)
print(SpacePoint.counter)

for i in range(400):
    p = SpacePoint(i*0.5, i, i+1)

print(SpacePoint.counter)


#clases con mètodos estáticos..

class A(object):
    @staticmethod
    def write(message):
        print( message)

A.write('Hello')

a = A()
a.write('Hello again')

#CLASE PARA LA FUERZA DE GRAVEDAD ENTRE DOS CUERPOS 

class Gravity(object):
    """fuerza de gravedad entre dos objetos físicos"""
    
    def __init__(self, m, M):
        self.m = m              #masa del objeto 1
        self.M = M              #masa del objeto 2
        self.G = 6.67428E-11    #constante de gravitación universal, m**3/kg/s**2
    
    def force(self, r):
        G, m, M = self.G, self.m, self.M
        return G*m*M/r**2
    
    def visualize(self, r_start, r_stop, n=10000):
        import numpy as np
        import  matplotlib.pyplot as plt 
        r = np.linspace(r_start, r_stop, n)
        g = self.force(r)
        title = 'fuerza de gravedad: m=%g, M=%g' % (self.m, self.M)
        plt.plot(r, g)
        plt.title(title)
        
masa_luna= 7.35E+22; masa_tierra = 5.97E+24
gravity = Gravity(masa_luna, masa_tierra)
r = 3.85E+8 #distancia entre la luna y la tierra 
Fg= gravity.force(r)
print('el valor de la fuerza entre la luna y la tierra va como: %g Newtons' %(Fg))
gravity.visualize(1, 250)




# trabajando con intervalos aritméticos 

class IntervalMath(object):
    def __init__(self, lower, upper):
        self.lo = float(lower)
        self.up = float(upper)
    
    def __add__(self, other):
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return IntervalMath(a + c, b + d)
    
    def __sub__(self, other):
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return IntervalMath(a - d, b - c)
    
    def __mul__(self, other):
       
        #para extender el método a elementos que no tienen un intervalo como tal
        #sino que tienen la caracteristica nada mas de flotante, lo único que tenemos que hacer es 
        #establecer un intervalo con los mismos límites inferior y superior, de la forma..
        
        if isinstance(other, (int, float)):
            other = IntervalMath(other, other)
        a, b, c, d = self.lo, self.up, other.lo, other.up
        
        return IntervalMath(min(a*c, a*d, b*c, b*d), 
                             max(a*c, a*d, b*c, b*d))
    
    def __truediv__(self, other):
        a, b, c, d = self.lo, self.up, other.lo, other.up
        #[c,d] no pueden contener valor cero 
        if c*d <= 0:
            raise ValueError\
                ('el intervalo %s no puede ser denomidador dado que '\
                 'contiene un valor cero' % other)
        return IntervalMath(min(a/c, a/d, b/c, b/d),
                            max(a/c, a/d, b/c, b/d))
    
    def __rmul__(self, other):
        # en el caso de tener entradas enteras multimplicadas por los intervalos 
        if isinstance(other, (int, float)):
            other = IntervalMath(other, other)
        return other*self
    
    def __pow__(self, exponent):
        if isinstance(exponent, int):
            p= 1
            if exponent > 0:
                for i in range(exponent):
                    p = p*self
            
            elif exponent < 0:
                for i in range(-exponent):
                    p = p*self
                    
                p =1/p
            else: #para expoenente ==0
                p = IntervalMath(1, 1)
            return p
        else:
            raise TypeError('el expoennte debe ser entero')
            
    
    def __float__(self):
        return 0.5*(self.lo + self.up)
    
    def __str__(self):
        return '[%g, %g]' %(self.lo, self.up)
    


I= IntervalMath
a = I(-3,-2)
b = I(4,5)
print(a + b)

expr = 'a + b', 'a - b', 'a*b', 'a/b'
for e in expr:
    print( '%s =' % e, eval(e) )







x = 1
c = eval('x + 1')
print(c)

g = 9.81
y_0= I(0.99, 1.01)
Tm = 0.45
T = I(Tm*0.95, Tm*1.05)
print(T)

g = 2*y_0/T**(2)
print('g vale:', g)

#implementado la clase en el volumn de una esfera
from math import pi
Rm = 6
R= I(Rm*0.9, Rm*1.1)
V= (4./3)*pi*R**3
print(V)
print(float(V))
R= float(R)
V= (4./3)*pi*R**3
print(V)










