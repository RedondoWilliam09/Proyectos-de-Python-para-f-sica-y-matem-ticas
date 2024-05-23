# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 10:07:04 2021

@author: william
"""

import numpy as np
from matplotlib import *
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
import time, glob, os


#eliminar RCHIVOS ANTIGUOS
for filename in glob.glob('animacion_matl'):
    os.remove(filename)   

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
fig= plt.figure()
plt.axis([x[0], x[-1], -0.1, max_f])
lines=plt.plot([], [])
plt.xlabel('x')
plt.ylabel('f')


def init():
    lines[0].set_data([],[]), #plot vacío
    return lines

#función que regresa un cuadro en la pelicula 

def frame(args):
    frame_no, s, x, lines= args
    y= f(x, m, s)
    lines[0].set_data(x,y)
    return lines

#construir una lista con todos los argumentos de los cuadros de la función 

#cada llamda envía un numero de cuadro, un valor de s, un array x, y una linea de lista

all_args = [(frame_no, s, x, lines)
            for frame_no, s in enumerate(s_values)]

#correr la animación

anim = animation.FuncAnimation(fig, frame, all_args, interval=150, 
                              init_func=init, blit= True)

#construir la pelicula en archivo mp4

anim.save('animacion_matl.gif', fps=7)
plt.show()








