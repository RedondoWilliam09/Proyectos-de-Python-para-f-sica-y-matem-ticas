# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 06:04:02 2021

@author: william
"""

import numpy as np
import matplotlib.pyplot as plt


def f1(t):
    return t**2*np.exp(-t**2)
def f2(t):
    return t**2*f1(t)

t= np.linspace(0,3,51)
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

