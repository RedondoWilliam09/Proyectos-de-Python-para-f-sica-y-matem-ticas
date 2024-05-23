# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 08:05:48 2021

@author: william
"""

#podemos construir un diccionario con claves los nombres del parámetro y el valor los valores de las densidades

def read_densities(filename):
    infile = open(filename, 'r')
    densities= {}
    for line in infile:
        words = line.split()
        density = float(words[-1])
        
        if len(words[:-1]) ==2:
            substance = words[0] + '' + words[1]
        else:
            substance = words[0]
        
        densities[substance] = density
    infile.close()
    return densities

datos= read_densities('D:\desktop\curso phyton física\datos.dat')

#para que funcione extrar datos de los archivo es necesario agregar toda la dirección 

print(datos)
