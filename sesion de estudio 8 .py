#la libreria scitoolos nos permite  incluir funciones tipo string para 
#poderlas regresar como funciones de x en python
import scitools
from scitools.StringFunction import StringFunction
from math import *

formula= 'exp(x)*sin(x)'
f= StringFunction(formula) # me regresa la fórmula como función de x

print(f(0))
print(f(1))
print(f)

#pòdemos hacer el mismo tratamieno con mas variables independientes 

g= StringFunction('Aexp(-a*t)*sin(omega*x)',
independent_variable= 't',
A=1, a=0.1, omega= pi, x=0.5)
print(g)
#podemos después varias los valores de los parámetros 
#con:
    
g.set_parameters(omega=0.1)
g.set_parameters(omega=0.1, A=5, x=0)
print(g) #cambian los valores en g 

import argparse 

