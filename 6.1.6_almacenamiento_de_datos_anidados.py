# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 08:27:29 2021

@author: william
"""

#el algoritmo es el siguiente:
# examinar la primera línea: dividir en palabras e inicializar
#  un diccionario con la propiedad de nombre y clave en un diccionario vacío {}
#  como valor 
 

# por cada una de las líneas restantes en el archivo:
#     dividir la línea en palabras 
#     para cad apalabra después de la primera:
#         si la palabra no es 'no':
#             transformar la palabra en un número real 
#             y almacenar el numero en el diccionario relevante 
            

#☺otra herramienta imprtante son los diccionarios anidados, es decir, diccionarios 
# de diccionarios 
# un ejemplo es <

d = {'key1':{'key1':2, 'key2':3}, 'key2':7}

print(d['key1'])
print(type(d['key1']))

print(d['key1']['key1'])
print(d['key1']['key2'])

