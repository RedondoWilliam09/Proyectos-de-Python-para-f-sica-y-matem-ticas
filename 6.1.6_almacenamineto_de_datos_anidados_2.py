# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:18:41 2021

@author: william
"""

infile = open('D:/Desktop/curso phyton física/table2.dat', 'r')
lines = infile.readlines()
infile.close()
data= {}          #data[property][medida_no] = propertyvalue
first_line = lines[0]
properties = first_line.split()

for p in properties:
    data[p]= {}

for line in lines[1:]:
    words = line.split()
    i = int(words[0])  #número de medida
    values= words[1:]  #propiedad valor 
    for p, v in zip(properties, values):
        if v != 'no':
            data[p][i]= float(v)

#para el cálculo del valor medio:
    
for p in data:
    values = data[p].values()
    data[p]['mean'] = sum(values)/len(values)

for p in sorted(data):
    print('Mean value of property %s = %g' % (p,data[p]['mean']))   
    
    
    
    
    
    
    
    
    
    
    
    
    
    