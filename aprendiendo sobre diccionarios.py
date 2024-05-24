# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 08:00:51 2021

@author: william
"""

#28/08=2021

#temperaturas en varis ciudades 

temps = [13, 15.4, 17.5]

print("LA TEMEPRATURA DE lONDRES VA COMO:", temps[1])

#pero es mas conveniente utilizar un diccionario

temps = {'Oslo':13, 'london':15.4, 'Paris': 17.5}

#o de la misma forma 

temps = dict(Oslo= 13, London= 15.4, Paris= 17.5)

#podemos agregar mas 

temps['Madrid']= 26.0

print(temps)
print(temps['London'])

#OPERACIONES CON DICCIONARIOS 

#podemos usar las claves de los diccionarios de la forma


for ciudad in temps:
    print ('la temperatura en %s es %g' % (ciudad, temps[ciudad]))

#con los condicionales

if 'Berlin' in temps:
    print ('Berlin', temps['Berlin'])
else:
    print('no hay datos de temperatura para Berlin')

print('Oslo' in temps)

#podemos extraer las claves en una lista

print(temps.keys())

#podemos extraer los valores en otra lista 

print(temps.values())

#podemos ordenar el orden en las listas de regreso 

for ciudad in sorted(temps):
    print(ciudad)
    

#podemos eliminar pares-valores

del temps['Oslo']
print(temps)
print(len(temps))

#podemos hacer una copia de un diccionario 

temps_copy = temps.copy()

del temps_copy['Paris']
print(temps_copy)

print(temps)

#polinomios con diccionarios 

#las listas y los diccionarios son onjetos mutables 

#podemos construir pares potencia-coeficiente 

p= {0:-1, 2: 1, 7: 3}

#podemos usar una lista pero para que coincida hacemos::

p= [-1,0,1,0,0,0,0,3]


#polinomio representado como un diccionario 

def eval_poli_dict(poly, x):
    sum= 0.0
    for power in poly :
        sum += poly[power]*x**power
    return sum

def eval_poly_dict2(poly, x):
    return sum([poly[power]*x**power for power in poly])

#podemos resumir aún mas
def eval_poly_dicts(poly, x):
    return sum(poly[power]*x**power for power in poly)


#para representar por medio de listas hacemos:

def eval_Poly_list(poly, x):
    sum= 0
    for power in range(len(poly)):
        sum += poly[power]*x**power
    return sum

print(eval_Poly_list([1,2],2))


j= [1,2,3,4]
print(j)
print(j[2])
print(j)

#diccionarios con claes de valor predeterminado

p1= {-3:2, -1:-1.5, 2:-2}






from collections import defaultdict

def polynomial_coeff_default():
    #valor predeterminado para polinomios de diccionario
    return 0.0
p2 =defaultdict(polynomial_coeff_default)
p2.update(p1)

p2=defaultdict(lambda: 0.0)

p2= defaultdict(float)

p2.update({2:8})
p2[1]
print(p2[1])  #me devuelve un valor de cero 
print(p2[0])
print(p2[2])
print(p2[-2])

print(p2)

#los diccionarios dse devuelven de una forma desordenada, podemos ordenarlos

for key in sorted(p1):
    print(key, p1[key]) #organiza las potencias de menor a mayor 
    
#hay una función que hace que se conserve el orden de un diccioario tal como fueron organizadas en la entrada

from collections import OrderedDict


p2= OrderedDict({-3:2, -1:-1.5, 2:-2})
print(p2)
p2[-5]= 6
print(p2)  #solo mantiene el orden 

p2= OrderedDict(p2)
print(p2)

for key in p2:
    print(key, p2[key])


#ejemplo

data= {'Jan 2': 33, 'Jan 16': 0.1, 'Feb 2': 2}

for date in data:
    print(date, data[date])

#de no aparecer el orden registrado hacemos

data = OrderedDict()

data['Jan 2']= 33
data['Jan 16'] = 0.1
data['Feb 2'] = 2
for date in data:
    print(date, data[date])

#para el uso de fechas y horas podemos usar una sintáxis propia para ello

import datetime

data = {}

d= datetime.datetime.strptime #forma corta
data[d('Jan 2, 2017', '%b %d, %Y')] = 33
data[d('Jan 16, 2017', '%b %d, %Y')] = 0.1
data[d('Feb 2, 2017', '%b %d, %Y')] = 2

for date in sorted(data):
    print(date, data[date])



#ALMACENAMIENTO DE DATOS DE ARCHIVO EN DICCIONARIOS 

#tenemos los siguientes datos
















    



