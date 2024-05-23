# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 09:05:26 2022

@author: william
"""

class Gravity(object):
    """fuerza de gravedad entre dos objetos físicos"""
    
    def __init__(self, m, M):
        self.m = m
        self.M = M
        self.G = 6.67428E-11
    
    def force(self, r):
        G, m, M = self.G, self.m, self.M
        return G*m*M/r**(2)
    
    
    def visualize(self, r_star, r_stop, n = 100):
        # G, m, M = self.G, self.m, self.M
        from matplotlib.pyplot import plot, title, ylabel, xlabel, axis, show
        import numpy as np
        R= np.linspace(r_star, r_stop, n)
        g = np.zeros(len(R))
        for i in range(len(R)):
            g[i] = self.force(R[i])
        
        # axis = ([-2, 2, -2, 2])
        plot(R, g)
        title('Fuerza de gravedad:  m = %g, M = %g' %(self.m, self.M))
        ylabel("F(N)")
        xlabel("r(m)")
        axis([r_star, r_stop, self.force(r_stop), self.force(r_star) ])
        show()     
        
        
        
        
       
        

masa_luna = 7.36E+22; masa_tierra = 5.97E+24
gravedad = Gravity(masa_luna, masa_tierra)
r = 3.85E+8
Fg = gravedad.force(r)

print('fuerza igual tierra-luna a = ', Fg,'Newtons')
gravedad.visualize(0.1,3.85E+8)

masa_pelota = 10; masa_pelota_2= 100
gravedad_2= Gravity(masa_pelota, masa_pelota_2)
r2 = 20
Fg2= gravedad_2.force(r2)
print('la fuerza entre las dopelotas es igual a:', Fg2, 'Newtons')
gravedad_2.visualize(0.1, 22)


