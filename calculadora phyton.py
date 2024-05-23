vo=5
g= 9.81
t= 0.6
y= vo*t - (1/2)*g*t**2
print(" en t= %g s, la altura de la bola es de %.2f m." % (t,y))
print("en t={t:f} s \n una bola con velocidad inicial v0={vo:.3E} m/s  \n localizada a una altura de {y:.2f} m " .format(t=t, vo=vo, y=y))



#criterios de asignación de variables, el signo = representa un criterio de asignación no de igualdad en programación, por ejemplo
y=3
print(y)
y=y+5
print(y)

#conversión de grados a farenhait

c= 21
F=(9/5)*c + 32 
print(F)


#para mas funciones matemática utilizamos la libreria math, podemos importarla toda

v0= 5
g= 9.81
yc= 0.2

from math import * 
# from math import math   ### en el caso de solo importar una parte de la libreria

t1= (vo - sqrt(vo**2 - 2*g*yc))/g
t2= (vo + sqrt(vo**2 - 2*g*yc))/g

print("en t=%g segundos y %g segundos, la altura equivale a: %g m." %(t1, t2, yc))


#calculando el sinh(x)

x= 2*pi 
r1= sinh(x) 
r2= (1/2)*(exp(x) - exp(-x))
r3= (1/2)*(e**(x) - e**(-x))

print(" %.16f , %.16f ,  %.16f "%(r1,r2,r3))

print((1/49)*49 , (1/51)*51)

c=21
print(type(c))
c=float(c)
print(type(c))
print(c)

#podemos utilizar funciones directas de redondeo

print(round(20,952235))
print(int(round(20.3461)))

print("operación con numeros complejos") 

u= 2.5 + 3j
v=2
w=u + v
print(w)

a= -2
b= 0.5
so= a + b*1j   #creación de un numero complejo de dos flotantes
s=complex(a,b)  # creación laterna 
print(s, so)

print(s*w)
print(s/w)
print(s.real)  #parte real de un numero complejo
print(s.imag)  #parte imaginaria de un numero complejo 
print(s.conjugate())  # el conjugado del complejo s


#funcion seno de un nuemro complejo 

from cmath import *

r1= sin(8j)
print(r1)

#otra forma es utilizando la relaciçon 
	#e^(iq)=cosq + isinq

q=8
print(exp(1j*q))
####
print(cos(q) + 1j*sin(q))

print(sqrt(-1))

a = 1; b = 4; c = 1 # polynomial coefficients
#from numpy.lib.scimath import sqrt
r1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
r2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
print(r1,r2)

