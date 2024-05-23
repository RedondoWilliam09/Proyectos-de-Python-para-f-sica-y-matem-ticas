# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 08:19:41 2021

@author: william
"""

from math import *
from sympy import *

def L3(x, epsilon=1.0E-6):
    x= float(x)
    i= 1
    term=(1.0/i)*(x/(1+x))**i
    s= term
    while abs(term)>epsilon:
        i += 1
        term=(1.0/i)*(x/(1+x))**i
        s += term 
    return s, i

print(L3(10, 0.0001)) #funciona perfecto
s, z= L3(10)
print(z)

def table2(x):
    for k in range(4, 14, 2):
        epsilon= 10**(-k)
        approx, n = L3(x, epsilon=epsilon)
        exact= log(1+x)
        exact_error= exact- approx
        print("epsilon= %8.2e, exact error: %8.2e, n: %5.1f" %(epsilon, exact_error, n))

table2(10)



#cadenas de documentación para funciones 
    #perimiten escribir información sobre en qué cosiste la función 

def C2F(C):
    """
    
me permite convertir grados celcius (C) a grados Fahrenheit.
    Parametros: c
    ----------
    C : describe la temperatura en grados celcius

    grados fahrenheit
    -------
    None.

    """
    

def line(x0, y0, x1, y1):
    """
    calcula el coeficiente a y b en la
    expresion matemática para la linea recta 
    y= m*x + b que pasa por los puntos (x0, y0) 
    y (x1,y1) 
    

    Parameters:
        (x0,y0): un punto en la línea (float).
        (x1,y1): otro punto sobre la línea (float)
    ----------
    x0 : punto en las ordenadas.
    y0 : punto en abscisas.
    x1 :punto 2 en ordenandas .
    y1 :puno 2 en adscisas,

    Returns: valor de las constantes 
    -------
    None.

    """
    a= (y1-y0)/float(x1-x0)
    b= y0- a*x0
    return a, b

print(line.__doc__)


#funciones como argumentos de funciones 

#podemos implementar un código para la segunda derivada de una función 

def diff2nd(f, x, h=1E-6):
    r= (f(x-h) - 2*f(x) + f(x + h))/float(h*h)
    return r

def g(t):
    return t**(-6)

t=1.2

d2g = diff2nd(g,t)
print("g'' (%f)= %f" %(t, d2g))

#comportamiento de la derivada numerica cuando h tiende a cero 

#queremos ver ese comportamiento:
    
for k in range(1, 15):
    h=10**(-k)
    d2g= diff2nd(g, 1, h)
    print("h= %.0e: %.5f" %(h, d2g))
    
#EL PROGRAMA PRINCIPAL 
#   veamos el siguiente programa 

def f(x):                       #en principal 
    e= exp(-0.1*x)
    s= sin(6*pi*x)
    return e*s
x=2
y=f(x)
print("f(%g)= %g" %(x,y))

#una forma más compacta para llamar funciones es utilizando funciones lambda

f= lambda x: x**2 + 4

#es el equivalente a decir:

def f(x):
    return x**2 + 4

#las funciones lambda se utilizan generalmente para definir rápidamente una 
#función como argumento a otra función 
# por ejemplo en nel paso de la  sugunda derivada podemos hacer:
     
d2= diff2nd(lambda t: t**(-6),1, h=1E-4)

#las funciones lambda también pueden guardar argumentos clave

d2= diff2nd(lambda t, A=1, a= 0.5: -a*2*t*A*exp(-a*t**2),1.2)

print(d2)



#ramificación:

#un ejemplo de ramificación son las funciones a trozos

def f(x):
    if 0 <= x <= pi:
        value = sin(x)
    else: value = 0
    return value

print(f(2*pi))
print(f(pi/2))

# trabajando con if y else 
C=1
#❤❤C= float(input("inserta el valor en grados celcius: "))
if C< -273.15:
    print(" %g grados celcius es no físico " %(C))
else:
    F= (9/5)*C + 32
    print(F)
print("fin del programa ")


#otro programa sería:
    
if C< -273.15:
    print(" %s en grados celcius carece de sentido físico" %(C))
F = (9/5)*C + 32
    #aunque se incumpla la primera condición siempre calculará F

#otra forma es la abreviatura else if o elif en donde podemos tener varios if que perimiten ramificaciones
#múltiples del programa 

#podemos verlo de nuevo con una función de sombrero o lo mismo, una función a trozos 

# if K(x):
#     if x < 0:
#         return 0.0
#     elif 0 <= x < 1:
#         return x
#     elif 1 <= x < 2:
#         return 2 - x
#     elif x >= 2:
#         return 0.0

#que el la forma más clara de plasmar la fnción en código
#podemos acortarlo haciendo:

def N(x):
    if 0 <= x < 1:
        return x
    elif 1 <= x < 2:
        return 2-x
    else: 
        return 0.0
    

#uno puede tener una asignación de valor a una variable que depende  de 
#una expresión booleana. se puede hacer por un if-else

#pero se puede abreviar de la forma:
    
def f(x):
    return (sin(x) if 0 <= x < 2*pi else 0)      

# de la misma forma:

f= lambda x: sin(x) if 0<= x < 2*pi else 0

print(f(3*pi))


#ejemplo de integración numerica 

#podemos utilizar la aproximación por regla de simpson 

# s= 0 
# for i in range(M,N):
#     s += q(i)

#la función de simpson puede ser codificada como:
    

def Simpson(f, a, b, n=500):
    h= (b-a)/n
    sum1 = 0
    for i in range(1, int(n/2) + 1):
        sum1 += f(a + (2*i - 1)*h)
    sum2=0
    for i in range(1, int(n/2)):
        sum2 += f(a + (2*i*h))
    
    integral =((b-a)/(3*n))*(f(a) + f(b) + 4*sum1 + 2*sum2)
    return integral
# def f(x):
#     c= x**2
#     return c
# Simpson(f(x), 0, 2, n=10)


# necesitamos integrar la función:

def h(x):
    return (3./2)*sin(x)**3



def application():
    print("integral de (1/2)*sin(x)**3  de 0 a pi")
    for n in 2, 6, 12, 100, 500:
        approx= Simpson(h, 0, pi, n)
        print("n= %3d, approx = %18.15f, error %9.2E" %(n, approx, 2-approx))

application()

#para vericiar mejor sobre el error en el método de simpson, podemos
#probar con un polinomio de segundo grado, en el que el resultado
#con el método de simpson es exacto, tenemos:

# def g(x):
#     return 3*x**2 - 7*x + 2.5

# def G(x):
#     return x**3 - 3.5*x**2 + 2.5*x

# def test_Simpson():
#     a= 1.5
#     b= 2.0
#     n=8
#     exact= G(b)-G(a)
#     approx =Simpson(g, a, b, n)
#     succes = abs(exact - approx) < 1E-14
#     if not succes:
#         print("Eror: no se puede integrar la función cuadrática de forma exacta")


#podemos ncluir g y G dentro de test_Simpson

def test_Simpson():
    
    def g(x):
        #función a integrar
        return 3*x**2 - 7*x + 2.5

    def G(x):
        #integración exacta de g
        return x**3 - 3.5*x**2 + 2.5*x
    
    a= 1.5
    b= 2.0
    n=8
    exact= G(b)-G(a)
    approx =Simpson(g, a, b, n)
    succes = abs(exact - approx) < 1E-14
    if not succes:
        print("Eror: no se puede integrar la función cuadrática de forma exacta")
    print("el error obtenido es 0")

#podemos comprimir aún más utililizando funciones lambda 

# def test_Simpson():
#     """VERIFICACIÓN DE QUE LOS POLINOMIOS DE SEGUNDO GRADO TIENEN INTEGRAL EXACTA"""
#     a= 1.5
#     b= 2.0
#     n= 8
#     g= lambda x: 3*x**2 - 7*x + 2.5 #función a integrar
#     G= lambda x: x**3 - 3.5*x**2 + 2.5*x #integral de g
#     exact= G(b) - G(a)
#     approx= Simpson(g, a, b, n)
#     success= abs(exact - approx) < 1E-14 # nunca usar use== for en flotantes
#     assert success, msg 
    


test_Simpson()

print(18%2)
print(17%2) #denota mod(d,n), es el residuo de una división 























