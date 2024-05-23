# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 20:27:19 2021

@author: william
"""

# integración numérica con python 

#utilizando la regla trapezoidal ...

def trapezoidal(f, a, x, n):
    h= (x - a)/float(n)
    I= (0.5)*f(a)
    for i in range(1,n):
        I += f(a + i*h)
    I += 0.5*f(x)
    return I

#al definir la clase integral tneemos...

class Integral(object):
    def __init__(self, f, a, n=100):
        self.f, self.a, self.n = f, a, n
    
    def __call__(self, x):
        return trapezoidal(self.f, self.a, x, self.n)
    
from math import sin, pi
G= Integral(sin, 0, 200)
value= G(2*pi)
print(value)

#un calculo equivalente es..
value2 = trapezoidal(sin, 0, 2*pi, 200)
print(value2)


#verificación vía cálculo simbólico 

#podemos usar sympy para calcular la integral y despues regresar esa función como funcion operable en python 
# de la forma...

import sympy  as sp 
x = sp.Symbol('x')
f_expr= sp.cos(x) + 5*x
print(f_expr)

F_expr = sp.integrate(f_expr, x)
print(F_expr)

F= sp.lambdify([x], F_expr) #permite convertir F_expr en una funciónoperable 

print(F(0))
print(F(1))

#podemos escribir nuestra función de prueba como..


def test_Integral():
    
    #la regla trapezoidal es exacta para funciones lineales 
    
    import sympy as sp
    
    x= sp.Symbol('x')
    f_expr= 2*x + 5
    # convertimos la expresión sympy en una función simple de python
    f= sp.lambdify([x], f_expr)
    
    # encontrar la integral de f_expr y regresar una función simple de python F
    
    F_expr = sp.integrate(f_expr, x)
    F= sp.lambdify([x], F_expr)
    
    a= 2
    x= 6
    exact= F(x) - F(a)
    computed = Integral(f, a, n=4)
    diff = abs(exact - computed)
    tol = 1E-15
    assert diff < tol, ('error en la clase integral, diff = %s' %diff)

# la clase integral es inficiente pero mas que suficientemente rápida para
# graficar F(x,a) en función de x

#7.3.4 volviendo una estancia en un string 

# \la clase Y de la sección 7.2 puede ahora escribirse de la forma 

class Y(object):
    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81
    
    def __call__(self, t):
        return self.v0*t -0.5*self.g*t**2
    
    def __str__(self):
        return 'v0*t - 0.5*g*t**2; v0= %g' %self.v0


# colcando esta clase en acción tenemos

y= Y(1.5)
print(y(0.2)) 
print(y)

# 7.3.7 clases para polinomios 

class Polynomial(object):
    def __init__(self, coefficients):
        self.coeff= coefficients
    
    def __call__(self, x):
        
        """evalua el polinomio """
        
        s= 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s 
        
    def __add__(self, other):
        """regresa self + otro objeto como polinomio. """
        
        # Dos casos :
        
        # self: XXXXX
        # other: XXXXX
        
        
        # or:
        
        # self: XXXX
        # other XXXXXXX
        #COMIENZA CON LA LISTA MAS LARGA Y AGREGA EN OTHER
        
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:] #copiar
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
                result_coeff = other.coeff[:] #copiar
                for i in range(len(self.coeff)):
                    result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)
    
    #podemos definir un método de multiplicación 
    
    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        import numpy
        result_coeff = numpy.zeros(M +N +1)
        for i in range(0, M+1):
            for j in range(0, N+1):
                result_coeff[i+j] += c[i]*d[j]
        return Polynomial(result_coeff)
    
    #tambien podemos incluir un método pra diferenciar polinomios 
    #podmeos tomar dos enfoques diferenctes 
    
    def differentiate(self):
        """diferencia este polinomio reemplazando el original"""
        for i in range(1, len(self.coeff)):
            self.coeff[i - 1] = i*self.coeff[i]
        del self.coeff[-1]
    
    def derivate(self):
        """copia el polinomio y regresa su derivada"""
        
        dpdx = Polynomial(self.coeff[:])#hace una copia
        dpdx.differentiate()
        return dpdx

# para su implementación utilizamos los sigueinte polinomios...

p1 = Polynomial([1, -1])
p2 = Polynomial([0, 1, 0, 0, -6, -1])
# pk = Polynomial([0, 1, 0, 0, -6, -2])# la clase funciona incluso con 3 polinomios 
# p3 = p1 + p2 + pk
print(p1.coeff)
p3 = p1 + p2
print(p3) #solo me dá la ubicación del elemento en la ram 
print(p3.coeff) # de acuedo al constructor 
p4 = p1*p2
print(p4.coeff)

p5=p2.derivate()
print(p5.coeff)

#evaluando el valor x de los polinomiso tenemos ..
x= 0.5
p1_plus_p2_value = p1(x) + p2(x)
p3_value = p3(x)
print(p1_plus_p2_value - p3_value)

forma elegante de escribir polinomios 

        
    

 























