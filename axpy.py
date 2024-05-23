# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 10:39:29 2021

@author: william
"""
import time
import  matplotlib.pyplot as plt
import numpy as np
from memory_profiler import profile
from line_profiler import  *

@profile
def axpy1(a,x,y):
    r= a*x + y
    return r

x=y=np.r_[-100:100:10000000j]
axpy1(2,x,y)


@profile
def axpy2(a,x,y,r):
    r[:]=x
    r *=a
    r += y
    return r

r= np.zeros(10000000)
axpy2(2,x,y,r)

#plt.plot(x,axpy2(2,x,y,r))

#print(time.time())