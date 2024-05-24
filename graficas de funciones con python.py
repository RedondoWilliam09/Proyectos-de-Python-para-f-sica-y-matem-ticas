# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 08:58:01 2021

@author: william
"""

# bosquejo de una curva básica 

from matplotlib.pylab import *
#matplotlib.rcParams['text.usetex']= True 

def f(t):
    return t**2*exp(-t**2) 
t=linspace(0,3,31)
y=zeros(len(t))
for i in range(len(t)):
    y[i]= f(t[i])

plot(t,y)
#los ajustes de la crva se agregan después del comando plot 

xlabel("t")
ylabel("y")
legend(['$t^2e^{-t^2}$'])
axis([0, 3, -0.05, 0.6])
title('distribución de velocidades $t^2e^{-t^2}$')

show()
savefig('curva exponencial.png')


#graficando multiples curvas 


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
legend(["$t^2e^{-t^2}$","$t^4e^{-t^2}$"])
title("gráfica de dos curvas en el mismo plano ")
show()

import numpy as np
import matplotlib.pyplot as plt


def f1(t):
    return t**2*exp(-t**2)
def f2(t):
    return t**2*f1(t)

t= linspace(0,3,51)
y3= f1(t)
y4= f2(t)

fig = plt.figure(figsize=(12,12)) #ajusta el tamaño de las gráficas
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 2, 1)
plt.plot(t, y3, 'r-', t, y4, 'bo')
plt.xlabel('tiempo (s)')
plt.ylabel('posición (m)')
plt.legend(["t^2*exp(-t^2)", "t^4*exp(-t^2)"])
plt.axis([t[0], t[-1], min(y3)-0.05, max(y4)+0.5])
plt.legend(["distribución n", "distribución m"])
plt.title('curva de posición-tiempo')


plt.subplot(2, 2, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')
plt.title('función sinusoidal')

plt.subplot(2, 2, 3)
plt.plot(x1, y1, 'o-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2, 2, 4)
plt.plot(x2, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')
plt.title('función sinusoidal')
plt.show()

