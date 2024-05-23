

#LA FUNCIÓN MAGIC EXEC

#PODEMOS EJECUTAR UNA CADENA DE CODIGO EN PHYTON Y NO SOLO UNA EXPRESION 
from math import *
# formula= input("inserta tu fórmula")
# code ="""
# def f(x):
#     return %s
# """ % formula
# exec(code)
# x= 1
# print(f(x))
# s=f(1)
# print(s)

from scitools.StringFunction import StringFunction

formula= "exp(x)*sin(x)"
f= StringFunction(formula) #me regresa una funcíon de x

print(f(0))
