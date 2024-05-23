# -*- coding: utf-8 -*-


"""
Created on Thu Mar  3 21:12:30 2022

@author: william
"""
import numpy as np
import copy
n =10

l_i = 1
l_s = 4*np.pi
c_ls = 60
xp= np.linspace(l_i,l_s,c_ls)

xp2 =copy.copy(xp)


F = np.ones(n+1) 
G= np.zeros(len(xp))
x = np.ones(n+1)
for i in range(len(x)):
    x[i] = round(np.random.uniform(l_i, l_s),2)
    print('x[i]=',x[i])
    print('x[i-1]=',x[i-1])

for i in range(len(x)):
    for j in range(len(x)):
        if i != j:
            while (x[i]==x[j]):
                x[j] = round(np.random.uniform(l_i, l_s),2)
                print('se utilizó el bucle')
print(xp, 'aquìii')
xp = x 
print(xp, 'aquìii')           
yp = np.sin(xp)
xp = xp2
print(xp,'aquìii')
print(xp2, 'aquìii2')
yp2 = np.sin(xp)


print(yp2)
print('--------------------')

print('x=',x)

for k in range(len(xp)):
    for i in range(n+1):
        print('G[k]=', G[k], 'K inicio=', k)
        print('i =', i)
        print('x[i]=',x[i])
        for j in range(n+1):
            print('j_0 =', j)
            if x[i] != x[j]:
                print('xp(i)=', x[i], 'xp(j)=', x[j])
                c = x[i]- x[j]
                print('c=',c)
                if c != 0:
                    print('j=', j)
                    dl = (((xp[k] - x[j])/c))
                    print('dl=', dl)
                    F[i] *= dl
                    print('F=',F)
                        
        print('f[i]=', yp[i])
        F[i] = F[i]*yp[i]
        G[k] += F[i]
        print('F[i] producto =',F[i])
        print('G[k]==', G[k], 'k =', k)
        print('valor de  la matriz G=',G)
    F = np.ones(n+1) 
    print('la matriz G ahora se actualiza a =', G)
    print('siguiente ieración------------------+++++++++++++++')
        
print('Gtotal=',G)    
print(x) 
print(xp) 
print(yp)
print(F)        
from matplotlib.pylab import *

for i in range(len(xp)):
    print('xp=',xp[i], 'yp=',yp2[i], 'G=',G[i])

plot(xp, yp2)
plot(xp, G)
show()
   

#print(F)