#continuación estudio de listas con bucles 

#trabajando con datos booleanos 
    #en este caso son operadores de comparación los que se trabajan y no solo aplica para el 
    #caso de datos numericos
#algunos ejemplos son:


x=0; y=1.2
print(x>=0 and y<1)

print(x>=0 or y<1)
print(x>0 or x<1)
print(x>0 or not y>1)
print(-1<x<=0)
print(not(x>0 or y>0))

    #en el último ejemplo lo que hay dentro del parentesis de not es verdadero
    #porque hay un or y almenos una de las condicioens es cierta
    #pero not convierte ese true en un false 


#todos los objetos en phyton son boolenos excepto los false 
print("tipo de los objetos" )
s= "some string"
print(bool(s))

L=[]
print(bool(s))


#podemos implementar los bucles para expresar sumas de términos en matemáticas en phyton 
# como es el caso de la expansión en series de potencias de la función seno

#acá tenemos que son necesarios dos instrumentos
    #1. un contador K
    #2. una variable de suma, que almacena los términos que se acomulan uno a la vez


#luego tenemos :

from math import *

x= pi/2 #asignamos cualquier valor a x 
N=25  #es la máxima potencia en la suma 
k=1  # k empieza con un valor de 1
s=x   # se asigna a la variable s el valor de x
sign=1

while k<N:
    sign=-sign
    k=k+2
    term=sign*x**k/factorial(k)
    s=s + term 

print("sin(%g) = %g (aproximando con %d términos )" %(x, s, N ))

#☺uso de las listas 

#unos ejemplos son:

c=[-10, -5, 0, 5, 10, 15, 20, 25, 30]
print(c)

c.append(35)
print(c)
c.insert(8,13)
print(c)

c= c + [40, 45]
print(c)
print(c.index(10)) # me devuelve el índice en el cual está ubicado el elmento en la lista 
print(10 in c)
print(100 in c)
print(c[-1]) #último elemento de la lista
print(c[-5])  #penúltimo elemento de la lista 


#podemos agregar elementos a las listas utilizando un ciclo while 

c= []
c_value= -50
c_max= 200
while c_value <= c_max:
    c.append(c_value)
    c_value += 2.5  # abreviacion del incremento c + dc con dc = 2.5
print(c)

#podemos asignar valores equevalentes a los elemento de la lista, parecido a los diccionarios

somelist = ["book.tex", "book.log", "book.pdf"]
texfile, logfile, pdf = somelist
print(texfile)
print(logfile)
print(pdf)



#implementacioón del ciclo for 

degrees= [0, 10, 20, 40, 100]
for c in degrees:
    print("elemnto de lista", c)

print("la lista tiene grados:", len(degrees), "elementos")


#podemos construir tablas haciendo uso del ciclo for 


print("----------------")
e= []
c_value= -20
c_max= 40
while c_value <= c_max:
    e.append(c_value)
    c_value += 5  # abreviacion del incremento c + dc con dc = 2.5
print(e)


print("----------------")
for d in e:
    F= (9/5)*d + 32
    print("%5d    %5.1f" %(d,F))

print("--------------")


#podemos implementar lo que tenemos en el ciclo for en el ciclo while 

e #solo reslato que estoy trabajando con la lista guardada en la variable e
index = 0
print("   C       F")
while index < len(e):
    h= e[index]
    F=(9/5)*h + 32
    print("%5d   %5.1f" %(h, F))
    index += 1
    
print("-------------")

















