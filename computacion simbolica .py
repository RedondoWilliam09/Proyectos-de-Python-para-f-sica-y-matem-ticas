
#también podemos hacer computación sombólica en phyton 


from sympy import *


	#symbols, # define mathematical symbols for symbolic math
	#diff, # differentiate expressions
	#integrate, # integrate expressions
	#Rational, # define rational numbers
	#lambdify, # turn symbolic expressions into Python functions

t, vo, g = symbols("t vo g")
y= vo*t -Rational(1,2)*g*t**2
dydt= diff(y,t)
print(dydt)
print("la aceleracion va como: ", diff(y,t,t))
