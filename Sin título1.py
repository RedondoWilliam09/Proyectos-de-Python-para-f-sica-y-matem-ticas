# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 11:02:58 2022

@author: william
"""

print(5*0.6 - 0.5*9.81*0.6**2)

print(1*0.1 - 0.5*9.81*0.1**2)

v0= 5
g= 9.81
t = 0.6
y= v0*t -0.5*g*t**2
print(y)

print('AT t= %g s, the height of the ball id %.2f m.' %(t,y))

