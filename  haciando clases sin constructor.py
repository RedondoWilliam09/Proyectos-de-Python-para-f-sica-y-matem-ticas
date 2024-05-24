# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:50:24 2021

@author: william

Resoloviendo problemas simples implementando clases sin constructor

_______________________________________________________________
"""




def value(self, t):
    return self['v0']*t - 0.5*self['g']*t**2

def formula(self):
    print('v0*t - 0.5*g*t**2: v0= %G' % self['v0'])

# podemos colocar las funciones en un módulo Y 


y= {'v0':4, 'g':9.81} #hacemos una instancia 
y1= value(y,2)
print(y1)
y2= formula(y)



#7.1.6. CIERRES

def generate_y():
    v0 = 5
    g = 9.81
    def y(t):
        return v0*t - 0.5*g*t**2
    return y
y= generate_y()
print(y)
print(y(1))

# podemos especificar v0 como argumento de generate_y


def generate_y(v0):
    g = 9.81
    def y(t):                   #función cierre 
        return v0*t - 0.5*g*t**2
    return y

y1 = generate_y(v0=1)
y2 = generate_y(v0= 5)

print(y1(1))
print(y2(1))

#generando múltiples cierres en una función 

def generate():
    return [lambda t: (v0, t) for v0 in [1,1,5,10]]

funcs = generate()  #lista de funciones con un aegumento 

for func in funcs:
    print(func(1))
    
# pero es mas conveniente

def generate():
    return [lambda t, v0 = v0: (v0, t) for v0 in [0, 1, 5, 10]]



funcs = generate()
for func in funcs:
    print(func(2))

# 7.2.3. modelando un circulo con clases 

import numpy as np


class Circle(object):
    def __init__(self, x0,y0,R):
        self.x0, self.y0, self.R = x0, y0, R
    
    def area(self):
        return np.pi*self.R**2
    
    def circumference(self):
        return 2*np.pi*self.R
    
    

c= Circle(2, -1, 5)
print('A circle with radius %g m  at (%g, %g) has area %g m^2' % \
      (c.R, c.x0, c.y0, c.area()))

    
#PODEMOS IMPLEMENTAR UNA FUNCIÓN DE PRUEBA PARA VERIFICAR 
#   QUE LA CLASE CIRCLE ES CORRECTA 


def test_Circle():
    R=2.5
    c = Circle(7.4, -8.1, R)
    
    from math import pi 
    expected_area = pi*R**2
    computed_area = c.area()
    diff = abs(expected_area - computed_area)
    tol = 1E-14
    assert diff < tol, 'bug in  Circle.area, diff = %s' %diff
    
    expected_circumference = 2*pi*R
    computed_circumference = c.circumference()
    diff = abs(expected_circumference - computed_circumference)
    assert diff < tol, 'bug in Circle.circumference, diff = %s' % diff
    

d= test_Circle()
print(d)
#la prueba me arroja un dato string none 


#en lugar de usar una clase, podríamos simplemente usar una lista con los parámetros 

x0, y0, R = 2, -1, 5
circle = [x0, y0, R]

def Area(c):
    from math import pi
    R =c[2]
    return pi*R**2


def circunference(c):
    from math import pi
    R= c[2]
    return 2*pi*R

#también podríamos representar el círculo mediante diccionarios 

circle = {'center': (2,-1), 'radius': 5}

def area(circle):
    from math import pi
    R = circle['radius']
    return pi*R**2

def circumference(circle):
    from math import pi
    R = circle['radius']
    return 2*pi*R


print(circumference(circle), 'en unidades de metros ')

print(area(circle), 'en unidades de m^2')


d= circle['center']
print(d)


