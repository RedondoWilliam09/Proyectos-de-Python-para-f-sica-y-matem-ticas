



"""
Practicando la notación simbólica

______


"""


from math import *
from sympy import *

t, vo, g = symbols("t vo g")
y= vo*t -Rational(1,2)*g*t**2
dydt= diff(y,t)
print(dydt)
print("la aceleracion va como: ", diff(y,t,t))

v=lambdify([t, vo, g], dydt)
s = v(0, 5, 9.81)
print(s)

print(v(2, 5, 9.81))


#podemos resolver ecuaciones diferenciales y trabajar con series de taylos desde phyton 

roots= solve(y,t)
print("las raices a nuestro problema son : " )
print(roots)


#podemos verificar si las soluciones obtenidas son las correctas a traves de 

print(y.subs(t, roots[0]))
print(y.subs(t, roots[1]))

# podemos probar para resolver un polinomio de Taylor 
#entonces tenemos:
    

f= exp(t)
print(f.series(t, 0, 3)) #los últimos dos denotan el intervalo de la expansión 

f=exp(sin(t))
print(f.series(t, 0, 12))


#para tener una salida con los resultados en latex también es posible 
#hacemos:
    
print("en latex tenemos:")


print(latex(f.series(t, 0, 7)))


#podemos tambien simplifar expresines em  phyton 

x,y = symbols("x y") 
f= -sin(x)*cos(y) + cos(x)*cos(y)
print(simplify(f))
print(latex(simplify(f)))



#programa para evaluar la posición de una bola que se mueve en un movimiento parabólico 

g = 9.81 #(m/s^2)
v0 = 15  #(km/h)
theta = 60 #grados
x = 0.5 #m
y0 = 1  #m 
print("v0=  %.1f km/h ,theta= %d , grados y0= %.f m , x= %.1f m" %(v0, theta, y0, x))

#necesitamos convertir v0 a m/s y theta a radianes

v0= v0/3.6
theta= theta*(pi/180)

y= x*tan(theta) - (1/2*v0**2)*(g*x**2)/((cos(theta))**2) + y0
print("y= %.1f m" %y)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    