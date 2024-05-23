# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 22:31:04 2021

@author: william
"""

class Myclass(object):
    def __init__(self):
        self.data = 2
    
    def __str__(self):
        return 'In __str: %s' % str(self.data)



a= Myclass()
print(a)
a
