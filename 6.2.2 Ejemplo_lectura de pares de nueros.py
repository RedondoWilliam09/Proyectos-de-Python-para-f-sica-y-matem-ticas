# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 11:18:14 2021

@author: william
"""

#cargar el archivo en una lista de lineas 
with open('D:/Desktop/curso phyton física/read_pairs1.dat', 'r') as infile:
    lines = infile.readlines()

#analizar los contenidos de cada línea

pairs = []  #lista de (ni,n2) pares de números 
for line in lines:
    words = line.split()
    for word in words:
        word = word[1:-1]  #eliminar los parentesis 
        n1, n2 =word.split(',')
        n1= float(n1); n2 = float(n2)
        pair = (n1,n2)
        pairs.append(pair)  # agrega una 2- tupla a la ultima Fila
        print((n1,n2), 'es el par ordenado %g en la coordenada x y %g en la coordenada y' %(n1,n2))
print(pairs)


# si el archivo está separado solo por comas podemos hace

with open('D:/Desktop/curso phyton física/read_pairs2.dat', 'r') as infile:
    text = infile.read()
#text = text.replace(') ,', ')')
text = '[' + text + ']'
pairs = eval(text)
print(pairs)
