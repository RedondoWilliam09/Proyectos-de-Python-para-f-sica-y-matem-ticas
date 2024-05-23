# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 09:17:32 2021

@author: william
"""
import numpy as np
from matplotlib import *
# import time, glob, os 

# for name in glob.glob('animacion_02_08.pdf'):
#     os.remove(name)

def f(x, m, s):
    return (1.0/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/s)**2)

m = 0
s_max = 2
s_min = 0.2
x = np.linspace(m -3*s_max, m + 3*s_max, 1000)
s_values = np.linspace(s_max, s_min, 30)
# f is max for x=m; smaller s gives larger max value
max_f = f(m, m, s_min)

#construye primero la curva 

plt.ion()
y=f(x,m,s_max)
lines= plt.plot(x,y)
plt.axis([x[0], x[-1], -0.1, max_f])
plt.ylabel('f')
plt.xlabel('x')
plt.legend(['s=%4.2f' % s_max])

#mostrar el video, y hacer una secuencia de copias simultaneas

counter = 0
for s in s_values:
    y=f(x, m, s)
    lines[0].set_ydata(y)
    plt.legend(['s=%4.2f' % s ])
    plt.draw_all()
    plt.savefig('animacion_02_08%04d.gif' % counter)
    counter += 1









