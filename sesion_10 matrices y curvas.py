# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 06:37:20 2021

@author: william
"""


#CÁLCULO DE MATRICES Y TRAZADO DE CURVAS 

#podemos representar un vector como un par ordenado almacenado en una tupla o en una lista 

#matrices en python, diferentes a las lista 

#uso de lsitas para recopilar datos 

import numpy as np



#para trabajar con python en listas hacemos 
def f(x):
    return x**3
n=5
dx= 1/(n-1)
xlist=[i*dx for i in range(n)]
ylist= [f(x) for x in xlist]
pairs = [[x,y] for x, y in zip(xlist, ylist)]


#mylist= [2, 6.0, 'tmp.pdf', [0,1]]

#a= np.array(r) #convierte una lista en un array(matriz)

#para crear una matriz de ceros hacemos:
    
#a= np.zeros(n)

#en los array sus elementos son de tipo flotante, 
#podemos usar algunas entradas para manejar el tipo de elementos en el array

# con:
    
# a= np.zeros_like(c)

# también quereomso arrays con distribucion uniforme de elementos en el intervalo [p,n]
# llo hacemos con:
# a= np.linspace(p, q, n)

# a losl elementos de los array se accede igual que en las listas 

# a[i], a[1:-1], a[::4] (todos los elementos en intervalos de 4 elementos ), etc..

# se puede hacer también 
from numpy import *



#CALCULAR COORDENADAS Y VALORES DE FUNCIONES 

#PODEMOS TRABAJAR LAS LISTAS ANTERIORES +

x2= np.array(xlist) #convierto l lista en el array x2
y2= np.array(ylist)
print(x2)
print(y2)

#podemos trabajar directamente con aray de la forma:
print("-----------------")
n=len(xlist)
x2=np.linspace(0,1,n)
y2= np.zeros(n)
for i in range(n):
    y2[i]=f(x2[i])
print(y2)

#VECTORIZACIÓN 

#los bucles en matrices muy largas pueden ejecutarse muy lentamente,
# una gran ventaja con matrices es que podemos deshacernos de los bucles y aplicar directamente 
# f sobre el conjunto completo

y2=f(x2)
print(y2)
print("--------------")


#en el siguiente código se calcula cada elemento de la matrixz por separado 

from math import *
from numpy import *
x= np.linspace(0,2, 201)
r= np.zeros(len(x))
for i in range(len(x)):
    r[i]= sin(np.pi*x[i])*cos(x[i])*exp(-x[i]**2) + 2 + x[i]**2
    
print(r)

# dado que sin de math es diferente a el de numpy el ultimo si opera sobre matrices 
# podemos comprimir el bucle  haciendo:
    
#r= np.sin(np.pi*x)*np.cos(x)*np.exp(-x**2) + 2 + x**2

# np se refiere a la librería numpy
# al ser la ultima que se llamó todas son de ahí

#por tanto solo hacemos:

r= sin(pi*x)*cos(x)*exp(-x**2) + 2 + x**2

print("-------------")
print(r)

# reemplazar un bucle como el anterior,
#  para calcular r[i], por un vector/array como r 
#  es llmado vectorización, la versión de bucle a menudo se conoce 
#  como código escalar 
 
#por ejemplo tenemos:

    
N=5
x= np.zeros(N); y=np.zeros(N)
dx= 2/(N-1) #intervalo en las coordenadas de x
for i in range(N):
    x[i]= -1 + dx*i
    y[i]= math.exp(-x[i])*x[i]

print(y)  #esto es código escalar 

#mientras que la correspondiente versión vestorizada va como:
x= np.linspace(-1, 1, N)
y= np.exp(-x)*x
print(y)

#Nota: las listas comprimidas aún trabajan como código esclar ya que aún se trabaja
#con bucles for dentro de ellas

# las funciones destinadas a un argumento escalar funcionan correctamente
# para un argumento de matriz x, siempre y cuando las funciones se importen desde numpy

#al trabajar con arrays en funciones decimos que esas funciones están vectorizadas

#la vectorizacion acelera los programas de phyotn 


#trazado de curvas 

#graficando la siguiente función:
#from matplotlib import *
#from matplotlib.pylab import *
from matplotlib.pyplot import *
def f(t):
    return t**2*exp(-t**2)
t=linspace(0,3, 31)
y=zeros(len(t))
for i in range(len(t)):
    y[i]= f(t[i])
plot(t,y)
#show()

#para guardar la curva hacemos:

#incluir elementos en los gráficos 


xlabel("tiempo (seg.)")
ylabel("posición (m)")
legend(["t^2*exp(-t^2)"])
axis([0, 3, -0.05, 0.6]) #[tmin,tmax,ymin,ymax]
title("gráfica de posición-tiempo de una partícula")
show()

#graficando múltiples curvas

#graficando múltiples curvas 

def f1(t):
    return t**2*exp(-t**2)
def f2(t):
    return t**2*f1(t)

t= linspace(0,3,51)
y1= f1(t)
y2= f2(t)
plot(t, y1, "r-")
plot(t, y2, "bo")
xlabel("tiempo (seg.)")
ylabel("posición (m)")
legend(["t^2*exp(-t^2)","t^4*exp(-t^2)"])
title("gráfica de dos curvas en el mismo plano ")
show()



print("----------------")


#VARIOS CUADROS EN UNA IMAGEN 

figure() #nos constryuye una figura aparte 
subplot(2,2,1) #(filas. columnas, contador individual)
t= linspace(0,3,51)
y1= f1(t)
Y2= f2(t)

plot(t, y1, 'r-', t, y2, 'bo')
xlabel('tiempo (s)')
ylabel('posición (m)')
axis([t[0], t[-1], min(y2)-0.05, max(y2)+0.5])
legend(["t^2*exp(-t^2)", "t^4*exp(-t^2)"])
title('curva de posición-tiempo')

subplot(2,2,2)
t3=t[::4]
y3=f2(t3)

plot(t, y1, 'b-', t3, y3, 'ys')
xlabel('tiempo (s)')
ylabel('posición (m)')
axis([0, 4, -0.2, 0.6])
title("segunda gráfica")
legend(['t^2*exp(-t^2)','t^4*exp(-t^2)'])
show()

subplot(2,2,1)
t3=t[::4]
y3=f2(t3)

plot(t, y1, 'b-', t3, y3, 'ys')
xlabel('tiempo (s)')
ylabel('posición (m)')
axis([0, 4, -0.2, 0.6])
title("segunda gráfica")
legend(['t^2*exp(-t^2)','t^4*exp(-t^2)'])
show()


subplot(2,2,2)
t3=t[::4]
y3=f2(t3)

plot(t, y1, 'b-', t3, y3, 'ys')
xlabel('tiempo (s)')
ylabel('posición (m)')
axis([0, 4, -0.2, 0.6])
title("segunda gráfica")
legend(['t^2*exp(-t^2)','t^4*exp(-t^2)'])
show()
# subplot(3,1,3)
# t3=t[::4]
# y3=f2(t3)

# plot(t, y1, 'b-', t3, y3, 'ys')
# xlabel('tiempo (s)')
# ylabel('posición (m)')
# axis([0, 4, -0.2, 0.6])
# title("segunda gráfica")
# legend(['t^2*exp(-t^2)','t^4*exp(-t^2)'])
# show()



























