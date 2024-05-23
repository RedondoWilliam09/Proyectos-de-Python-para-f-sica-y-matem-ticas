# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 18:11:55 2021

@author: william
"""
import numpy as np
#MATRICES DE ORDEN SUPERIOR 

#consideremos unalista anidada o tabla  [C,F]

Cdegrees= [-30 + i*10 for i in range(3)]
Fdegrees= [(9/5)*C + 32 for C in Cdegrees]
table = [[C,F] for C, F in zip(Cdegrees, Fdegrees)]

print(table)

#esta lista anidada se puede convertir en una matriz

table2 = np.array(table)
print(table2)
print( type(table2))

#para la indexación de listas hacemos;
print(table[1][0])
print(table[2][1])

#la sintaxis funciona de la misma forma para matrices bidimensionales

print(table2[1][1])

#pero hay otra sintaxis

print(table2[1,0])
#podemos saber la dimension de la matriz
print(table2.shape)  #(i,j)

#matriz expresada como bucles anidados

for i in range(table2.shape[0]):
    for j in range(table2.shape[1]):
        print('table2[%d, %d] = %g' % (i, j, table2[i,j]))

#podemos extraer submatrices 

print(table2[0:table2.shape[0],1])  #segunda columna índice 1
print(table2[0:table2.shape[0],0])

print(table2[0: , 1]) #todos los elementos de la columna 1
print(table2[0: , 0]) #todos los elementos de la columna 0

print(table2[0 , :])  #todos los elementos de la fila 0
print(table2[1 , :])
print(table2[2 , :])

#creando una matriz mas grande 

t=np.linspace(1,30,30).reshape(5,6)  #lo ultimo denota la dimension del array 
print(t)

print(t[0,:])
print(t[1,:])
print(t[2,:])
print(t[3,:])
print(t[4,:])
print(t[:,0])
print(t[:,1])
print(t[:,2])
print(t[:,3])
print(t[:,4])
print(t[3,0])


print(t)


print('-----')

print(t[1:-1:2,2:])  # 1:-1:2 el dos en esta parte denota que se toman intercaladas las filas cada dos filas 
print(t[1:-1:1,3:])

print('----')
print(t[1:-1:2,])
print(t[2:4,:3])
print(t[3:,4:])
print(t[1:3,4:])

print('----')
print(t[:-2,:-1:2]) #en las columnas :-1:2 el dos se refiere a que tomamos las columnas intercaladas cada 2 columnas 


#de una forma más generalizada podemos hacer:


print(t[np.ix_([0,3],[1,2])])  #extraer los elementos de fila con índices 0 y 3 y los elementos de columna con índices 1 y 2

#podemos cambiar elementos de matriz de la forma:
 

t[np.ix_([0,3],[1,2])]=0
print(t)

#los recortes dan una vista de la matriz , no una copia de los valores

a= t[1:-1:2, 1:-1] #se reasignan los valores de t en la variable a, luego t cambia
print(a)

a[:,:]= -99 #cambiar todos lo elementos de a

print(a)
print(type(a))

print(t)




