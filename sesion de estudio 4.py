#comprensión de flujo de un programa 
    #tenemos el siguiente programa 
    
def F(C):
    F= (9/5)*C + 32
    return F

dC= 10
C= -30
while C<=50:
    print("%5.1f  %5.1f" %(C, F(C)))
    C += dC

# podemos utilizar:
#     http://www.pythontutor.com/visualize.html#mode=display 

# para verificar el flujo de un programa 

#____________

# en phyton existen variables globales y variables locales,
# las globales se encuentran fuera de las funciones contrario a las locales
# al llamar una funcion en phyton este empieza su búsqueda en las locales despues las globales despues las 
# funciones propias de phyton 

sum =500
print(sum)

def myfunc(n):
    sum= n + 1
    print(sum)
    return (sum)
sum = myfunc(2) + 1
print(sum) #nuevo valor en la variable global 


#cambiando variables globales dentro de funciones

a=20;  b=-2.5

def f1(x):
    a= 21
    return a*a + b

print(a)
 
def f2(x):
    global a 
    a= 21 #se cambia el valor de la variable global a 
    return a*x + b

print(a)

print(f1(3))
print(f2(3))
print(a)
print(a)


#funciones con varios argumentos

def yfunc(t, v0):
    g= 9.81
    return v0*t - (1/2)*g*t**2 #con t y v0 variables locales

#formas válidas de llmar la función:
    
y=yfunc(0.1, 6)
print(y)
y= yfunc(0.1, v0= 6)
print(y)
y=yfunc(t=0.1, v0= 6)
print(y)
y=yfunc(v0=6, t=0.1)
print(y)


#mas utilidades de las funciones en phyton 

def makelist(start, stop, inc):
    value= start 
    result= []
    while value <= stop:
        result.append(value)
        value= value + inc
    return result

mylist = makelist(0, 100, 0.2)
print(mylist)

#las funciones en phyton pueden devolver mas de un valor 

#por ejemplo:

def yfunc(t, v0):
    g= 9.81
    y= v0*t - (1/2)*g*t**2
    dydt= v0 - g*t
    return y, dydt

position, velocity = yfunc(0.6, 3)
print(position, velocity) # me devuelve posición y velocidad 
print(yfunc(0.6, 3))
print(position)
print(velocity) #son valores que
# se pueden imprimir aparte de la tupla que se genera

print("--------------")
#también podemos construir tablas de datos utilizando funciones :

t_value = [0.05*i for i in range(10)]
print(t_value) #lo que hace es crearme una lista de diez elementos 
for t in t_value:
    position, velocity, = yfunc(t, v0=5)
    print("t= %-10g position= %-10g velocity= %-10g" %(t, position, velocity))



#cuando una función nos devuelve valores multiples separados por una coma nos regresa una tupla
#podemos verlo en el siguiente código:
    
def f(x):
    return x, x**2, x**4

s=f(2)
print(s)
print(type(s)) # me devuelve una tupla

#PODEMOS CALCULAR SUMATORIAS EN PHYTON 

#ejemplo1:

s=0
for i in range(12):
    s +=i**4

print(s)

#ejemplo2

# s=0
# for i in range(1, n+1):
#     s +=(1/i)*(x/(1+x))**i

# print(s)

#para incluir los argumentos x y n podemos compactarlo en una función 

def L(x,n):
    s=0
    for i in range(1, n+1):
        s +=(1/i)*(x/(1+x))**i
    return s

#podemos saber el error en el calculo con la expresión en suma y la función 
from math import *
def L2(x, n):
    s=0
    for i in range(1, n+1):
        s += (1/i)*(x/(1+x))**i
    value_of_sum= s
    first_neglected_term =(1/(n+1))*(x/(1+x))**(n+1)
    from math import log
    exact_error=  log(1+x) - value_of_sum
    return value_of_sum, first_neglected_term, exact_error

value, approximate_error, exact_error = L2(3, 100)

print(L2(3,100))
print(value)

#funciones sin valores de retorno :
    
def table(x):
    print("\nx= %g, ln(1+x)= %g" %(x, log(1+x)))
    for n in [1, 2, 10, 100, 500]:
        value, next, error = L2(x,n)
        print("n= %-4d  %-10g (next term: %8.2e )" \
              "error: %8.2e" %(n, value, next, error))

table(10)
table(100)
table(10000)
#podemos verificar si un nomrbre se refiere a dos objetos o también si dos objetos tienen  el mismo contenido 

#por ejemplo:

a=1
b=a
print(a is b)  #a y b se refieren al mismo objeto 

c= 1.0
print(a is c)

print(a==c)


#argumentos de palabras clave 

def somefunc(arg1, arg2, kwarg1= True, kwarg2=0):
    print(arg1, arg2, kwarg1, kwarg2)

somefunc("hello", [1,2])
somefunc("Hello", [1,2], kwarg1="Hi")
somefunc("hello", [1,2], kwarg2= "Hi")
somefunc("Hello", [1,2], kwarg2="Hi", kwarg1=6)

#podemos mezclar los argumentos posicionales y de palabras clave si colocamos todos sus nombre

somefunc(kwarg2= "Hello", arg1="Hi", kwarg1=6, arg2=[1,2])


#funciones con parámetros predeterminados 

    #considere una funcion del tiempo que contiene los poarámetros A, a, omega:

        

print("-----------------------")
def f(t, A=1, a=1, omega= 2*pi):
    return A*exp(-a*t)*sin(omega*t)

v1=f(0.2) #solo la llamamos con el argumento de t
print(v1)
v2=f(0.2, omega=1)
print(v2)
v3=f(1, A=5, omega= pi, a=pi**2)
print(v3)
v4= f(A=5, a=2, t=0.01, omega= 0.1)
print(v4)
v5= f(0.2, 0.5, 1, 1)
print(v5)


#cálculo de una suma con tolerancia predeterminada 

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

print(L3(2)) #funciona perfecto
s, z= L3(2)
# print(s)
# print(n)

def table2(x):
    from math import log
    for k in range(4, 14, 2):
        epsilon= 10**(-k)
        approx, n = L3(x, epsilon=epsilon)
        exact= log(1+x)
        exact_error= exact- approx
        print("epsilon= %8.2e, exact error: %8.2e, n: %5.1f" %(epsilon, exact_error, n))

table2(10)
# print(2+2)
# print(2)























