# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 09:56:45 2021

@author: william
"""

#EJERCICIO 7.1 
#construye una clase que implmente la función: f(x; a,w) = e^(-ax)*sin(wx)

class F(object):
    def __init__(self, a,w):
        self.a, self.w =  a, w
     
    def funcion(self, x):
        self.x = x
        from numpy import sin, exp
        f = exp(-self.a*x)*sin(self.w*x)
        return f
    
    

from numpy import pi
v = F(a =1.0, w = 0.1)    
print(v.funcion(pi))
print(v.a)
v.a = 2
print(v.a)
print(v.funcion(pi))

print('para la función f = e^(-ax)sin(wx), con x = %g, w = %g,'\
             ' a = %g, el valor de la función es %g :' %(v.x, v.w, v.a, v.funcion(pi)))


    
#EJERCICIO 7.4
#clases para un rectángulo y un triángulo
# el propósito de este ejercicio es crear clases como la clase Circle de la sección 7.2.3. 
# para representar otras figuras geométricas: un rectángulo de ancho W, alto H, y esquina inferior izquierda: x0, y0
# y untriángulo general especificado por sus tres vértices (x0,y0), (x1,y1), (x2,y2), como se explica en el ejercicio 3.16
# proporcione tres métodos: init (para inicializar los datos geométricos), área y perímetro. Escriba las funciones de prueba 
# test_Rectangule() y test_Triangule para verificar los datos producidos por área y perímetro que coincidan 
# con valores exactos dentrto de una pequeña tolerancia 

class rectangle(object):
    def __Init__(self, w, h, x0, y0):
        self.w, self.h, self.x0, self.y0 = w, h, x0, y0
    
    def area(self, w, h):
        self.w, self.h = w, h
        return w*h
    
    def perimetro(self, w, h):
        self.w, self.h = w, h
        return 2*w + 2*h

class triangle(object):
    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1, self.x2, self.x3, self.y1, self.y2, self.y3 = x1, x2, x3, y1, y2, y3
    
    def area(self):
        from math import sqrt
        return (1/2)*(sqrt((self.x2 - self.x1)**2 + (self.y2-self.y1)**2))*(sqrt((self.x3 - (self.x2)/2)**2 + (self.y3-(self.y2)/2)**2))

    def  perimetro(self):
        from math import sqrt
        return  sqrt((self.x3 - self.x2)**2 + (self.y3-self.y2)**2) + \
            sqrt((self.x3 - self.x1)**2 + (self.y3-self.y1)**2) + \
                sqrt((self.x2 - self.x1)**2 + (self.y2-self.y1)**2)
        
        
g= triangle(0, 2, 1, 0, 0, 2)
print(g.area()) 
print(g.perimetro())

      











