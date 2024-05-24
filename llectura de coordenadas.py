# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 15:58:27 2021

@author: william
"""

# Impementación de un programa para la lectura de coordenadas en un plano

infile = open('D:/Desktop/curso phyton física/xyz.dat', 'r')
coor =[] #lista de tuplas (x,y,z) 
for line in infile:
    x_start = 2
    y_start = 16
    z_start = 31
    x= line[x_start+2:y_start]
    y= line[y_start+2:z_start]
    z= line[z_start+2:]
    print('debug: x="%s", y="%s", z="%s"' %(x,y,z))
    coor.append((float(x), float(y), float(z)))
infile.close()

import numpy as np

coor= np.array(coor)
print(coor.shape, coor)

