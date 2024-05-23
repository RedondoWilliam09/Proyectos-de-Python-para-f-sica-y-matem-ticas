# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:20:38 2022

@author: william
"""
import numpy as np
n = 2

xp= np.linspace(1,3,3)
yp = np.sin(xp)
    

f = np.zeros(len(xp))
F = np.ones(len(yp)) 
G= np.ones(len(yp))
for l in range(len(f)):
    for i in range(n+ 1):
        for j in range(n+1):
            if i != j or j!= i:
                dl = ((xp[l] - xp[j])/(xp[i]- xp[j]))
                F[l]  *= dl
        G[l] += F[l]*yp[i]    
    f[l] = G[l]
    print(f[l])

print(f)


