




from sympy import *

t, vo, g = symbols("t vo g")
y= vo*t -Rational(1,2)*g*t**2
dydt= diff(y,t)
print(dydt)
print("la aceleracion va como: ", diff(y,t,t))
v= input("la variable es : ")