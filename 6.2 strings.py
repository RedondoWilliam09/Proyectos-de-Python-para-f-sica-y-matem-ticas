# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 10:26:44 2021

@author: william
"""

#6.2 strings 

s= 'Berlin: 18.4 C at 4 pm'
print(s[8:])
print(s[8:12])


# también podemos hacer desde la derecha donde s[-1] es el último elemento, s[-2]
# el penú ltimo y así ..

print(s[8:-1])
print(s[8:-8])

print(s.find('Berlin')) #☺me regresa el índice donde el substring aparece primero, Berlin comienza en el índice 0
print(s.find('pm'))
print(s.find('Oslo')) # no se encuentra 

print('Berlin ' in s)
print('Berlin' in s)
print('Oslo' in s)

# utilizando una prueba if tenemos:

if 'C' in s:
    print('C found')
else:
    print('no C')

#para verificar si una cadena temrina con un string específico es:

print(s.startswith('Berlin'))
print(s.endswith('am'))

#podemos reemplazar un substring en un string 

print(s.replace('Berlin','Bonn'))  #solo funciona para imprimir 
print(s)  #el string s no cambia
print(s.replace(' ','_'))


#podemos reemplazar el tecto anted de los primeros dos puntos
print(s.replace(s[:s.find(':')], 'Bonn')) #reemplaza Berlin por Bonn

#la función s.slpit() divide el string n palabras en espacios 
print(s.split())
print(s.split(':'))


#podemos separar un archivo en líneas 
t= '1st line\n2nd line\n3rd line'
print(t)
print(t.splitlines())

#de mayusculas a minusculas 

print(s.lower())
print(s.upper())


# no se pueden reelplazar elementos en un string 
#pero podemos hacer 
g= s[:18] + '5' + s[19:]
print(g)


#podemos probar si una cadena contien digitos 

print('214'.isdigit())
print(' 214 '.isdigit())
print('2.14'.isdigit())

#podemos verificar si una caneda contine espacios 

print('    '.isspace())
print('   \n'.isspace())
print('  \n  '.isspace())
print('    \t    '.isspace())
print(''.isspace())  #string vacío

line= '    \n'
print(line.strip()=='') #verifica si en line hay cadenas vacias

# podemos elminar los espacios iniciales o finales de una acdena 
s= '    text with leading/trailing space   \n'
print(s.strip())   #elimina en ambos 
print(s.lstrip())  #lado izquierdo
print(s.rstrip()) #elimina en lado derecho


#tMBIÉN PODEMOS UNIR STRINGS

# t= delimiter.join(words)
# words= t.split(delimiter)

strings= ['Newton', 'Secant', 'Bisection']
t= ', '.join(strings)
print(t) #me genera un string separado por comas y espacios 

#eliminar las dos primeras palabras de una línea

line= 'This is a line of words separated by space'
words= line.split()
line2= ' '.join(words[2:])
print(line2)
print(words)


























