# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:26:05 2021

@author: william

Aprendiendo clases en python con problemas de física.


________________________________________


"""

#DESAFIO: FUNCIONES CON PARÁMETROS 

# creando una clase para la unción de posición 

class Y:
    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81
    
    def value(self, t):
        return self.v0*t - 0.5*self.g*t**2
    
    #podemos agregar más métodos y extender la clase, podemos incluir  el método fórmula 
    
    def formula(self):
        return 'v0*t - 0.5*g*t**2; v0 = %g' % self.v0
    

y= Y(3)   #esto es lo que define una instancia 
v= y.value(0.1) #utilizamos la instancia para calcular y(0.1, vo= 3)
print(v)
print(y.v0)  #podemos ver los valores de las instancias 


#las funciones en ls clases se demonimam comunmente métodos 
#las variables o (datos) en las clases se denominan atributos de datos 
#los métodos también se conocen como atributos de método 


#es una convención usar el constructor para inicializar las variables en la clase 

#una implementación es

y= Y(5)
t= 0.2
v= y.value(t)
print('y(t = %g; v0 = %g) = %g' % (t,y.v0, v))
print(y.formula())


#podemos asignar mas valores a la clase Y 

def diff(f, x, h=1E-5):
    return (f(x + h)-f(x))/h


y1= Y(1)
y2= Y(1.5)
y3= Y(-3)


dy1dt= diff(y1.value, 0.1)
dy2dt= diff(y2.value, 0.1)
dy3dt = diff(y3.value, 0.2)

print(dy1dt, dy2dt, dy3dt)






# las clases se les puede iuncluir una cadnea de doc para dejar en especifico de que trata la clase


# class Y(object):
#     """El movimiento Vertical de una Bola"""
#     def __init__(self, v0):
#         ...

#la información mas copleta puede iuncluir los métodos y como se usa la clase en una sesion interactiva


value = y.value(0.1)

#python traduce como 

value = Y.value(y, 0.1)


#cada objeto de python tinen un identificador único id(obj) que podemos imprimir para rastrerar quien es self 

class SelfExplorer(object):
    def __init__(self,a):
        self.a = a
        print('init: a = %g, id(self)= %d' % (self.a, id(self)))
    
    def value(self, x):
        print('value: a =%g, id(self = %d)' %(self.a, id(self)))
        return print(self.a*x)

s1 = SelfExplorer(1)

print(id(s1))

s2 = SelfExplorer(2)
print(id(s2))


# podemos ahora llamar a value

s1.value(4)
s2.value(5)
SelfExplorer.value(s2, 5)




y= Y(1.2)
print(y.__dict__)  #las instancias se almacenan como diccionarios 






















