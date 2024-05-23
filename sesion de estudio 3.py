

#la construcción range

#una de sus funciones de range es automatizar cuando se requieren listas de la forma 

c= []
for i in  range(-20, 45, 5):
    c.append(i)
    
print(c)

#en este caso el  contador solo va para números enteros
#como vamos hasta 40 tenemos que poner en el límite 45
#no funciona para decimales, solo genera nuemros en teros
#para generar decimales hacen¡mos c=-10 + i*2.5
    #tenemos
    
print("--------------------")

c= []
for i in range(0,21): #para range con dos parametros se omite el tamaño de paso cundo este vale 1
    d= -10 + i*2.5
    c.append(d)

print(c)

#podemos implementar bucle for con índices de lista 

    #para elvitar interactuar directamente con los valores en las listas, es mas conveniente 
    #trabajar con los índices de  las mismas

#tenemos el ejemplo:
    
print("------------------")


Cgrados= []
n= 21
C_min= -10
C_max= 40
dc= (C_max - C_min)/(float(n-1))  #que es el incremento en c
for i in range(0,n):
    c=-10 + i*dc
    Cgrados.append(c)

Fgrados= []
for c in Cgrados:
    F= (9/5)*c + 32
    Fgrados.append(F)

for i in range(len(Cgrados)):
    C= Cgrados[i]
    F= Fgrados[i]
    print("%5.1f   %5.1f" %(C, F))


print("·---------------------")


c=[0]*n
print(c)  #podemos construir una lista de solos ceros y despues ir llenando con 
                #los valores correctos 


print("-------------------")
n= 21
C_min= -10
C_max= 40
dc= (C_max - C_min)/(float(n-1))  #que es el incremento en c

Cgrados= [0]*n
for i in range(len(Cgrados)):
    Cgrados[i]= -10 + i*dc

Fgrados= [0]*n
for i in range(len(Cgrados)):
    Fgrados[i]= (9/5)*Cgrados[i] + 32

for i in range(len(Cgrados)):
    print("%5.1f   %5.1f" %(Cgrados[i], Fgrados[i]))


print("que es la misma lista pero ya trabajando sobre las listas inicialmente vacías y sobre sus índices")
print("-------------------")

    

#CAMBIANDO ELEMENTOS EN LAS LISTAS 
#para cambiar elementos d una lista, necesitamos trabajar directamente sobre 
#los indices de la lista osea com en el ejemplo Cgrados[i]

#podemos hacer lo siguiente:
    
for i, c in enumerate(Cgrados):
    Cgrados[i]= c + 5

print(Cgrados)


#dado que es frecuente que tengamos que sacar de una lista otras listas se puede abreviar de la 
#siguenet manera

Cgrados= [-5 + i*0.5 for i in range(n)]
Fgrados= [(9/5)*c + 32 for c in Cgrados]
C_mas_5= [c+5 for c in Cgrados]
print(Cgrados, Fgrados)

#podemos trabajar ambas listas simultaneamente 

print("------------")

for i in range(len(Cgrados)):
    print("%5.1f  %5.1f" %(Cgrados[i], Fgrados[i]))
    

#podemos usar la función zip para trabajar con varias listas simultaneamente 

print("--------------")
    
for C, F in zip(Cgrados, Fgrados):
    print("%5.1f  %5.1f" %(C, F))

#❤ anidación de listas 

Cgrados= range(-20, 41, 5)
Fgrados= [(9/5)*C + 32 for C in Cgrados]

table = [Cgrados, Fgrados]
print(table)

print(table[0][4])  #(0,i y 1,i son las entredas que tengo donde i es el recorrido tanto de la lista en cgrados como
                            #de la lista en Fgrados)
print(table[0]) # me recibe solo un parámetro tipo boolleano 0 o 1


#tambien podemos hacer:

print("----")

    #lo siguiente me genera una lista con los pares ordenandos [C, F]    

table=[]
for C, F in zip(Cgrados, Fgrados):
    table.append([C, F])

print(table)

print("------------")

#podemos abreviar aún mas si hacemos:

    #utilizanod una lista de comprensión

table=[[C, F] for C, F in zip(Cgrados, Fgrados)]
print(table)

print(table[3])


#la función  pprint imprime en cada línea un parde la tabla construida
import pprint

pprint.pprint(table)

#queda mas ordenado de la forma
for C,F in table:
    print("%5.1f  %5.1f" %(C,F))



print("----")

#también podemos modificar el formato de los elemento en las tablas
#haciendo:
    
    
   # la siguiente necesito de la heramienta scittols.pprint2
# import pprint, scitools.pprint2

somelist = [15.8, [0.2, 1.7]]
pprint.pprint(somelist)


#también podemos hacer

s=pprint.pformat(somelist)
print(s)

#esta última no sé como trabajarla 

print("-----------")

#extraer sublistas

A= [2, 3.5, 8, 10]
print(A[2:]) #☺desde A hasta el final de la lista 

print(A[1:3]) #el último elemento a llamar no está incluido 

print(A[:3]) #desde el elemento con ínidice 0 hasta el elemento con índice 2

print(A[1:-1]) #estrae todos menos el primer y último ellemnto de  la lista 

#en el caso de las listas anidadas tenemos

print(table[4:7][0:2]) #el primer intervalo hace una lista [[0, 32.0], [5, 41.0], [10,50.0]] con tres elementos. El segmento [0: 2] 
                        #actúa en esta sublista yselecciona sus dos primeros elementos, con índices 0 
print(table[4:])  #llama a todos los elementos de la tabla de los índices i= 4 para arriba 

#si modifica sublistas, la original permanece igual :

q= [1, 4, 3]
w= q[:-1]
print(w)
q[0]= 100
print(q)
print(w) # no  se modifica ya que está guardada antes de modificar q

print("---------")
print(A)
#podemos cirtar copias originales de una lista 

B=A[:]
C=A
print(B==A)
print(B is A)

print(table)


for C, F in table[Cgrados.index(10):Cgrados.index(35)]:
    print("%5.1f  %5.1f" %(C, F))

print(table)
print(Cgrados.index(10))



#podemos hacer lo mismo con el bucle for de la forma:

for C, F in table[6:11]:
    print("%5.1f  %5.1f" %(C, F))

#podemos trabajar con listas anidadas de la siguiente forma

#puntuaciones de jugadores.

score=[]
#puntuaciones del jugador 0
score.append([12, 16, 11, 12])
#puntuacionel del jugador 1
score.append([19])
#puntuaciones del jugador 2
score.append([6, 9, 11, 14, 17, 15, 14, 20])

#en este caso tenemos una lista con elementos como listas que determinan las 
#puntuaciones de cada jugador, cada fila de la lista score representa un jugador
#y cada columna de score rerpresenta la puntuación de los jugadores

#para organizar en tabla debemos utilizar bucles:

for p in range(len(score)):
    for g in range(len(score[p])):
        scores= score[p][g]
        print("%4d" %(scores,)) # la coma evita que las puntacines salgan en una línea
    print  #agrega una nueva linea despues despus de cada línea de la tabla (aunque al quitarlo no pasa nada)

#otra forma sería:
print("--------")
for player in score:
    for game in player:
        print("%4d" %(game))
    #me sale lo mismo si quito el print y la coma

#en un caso muy general, podemos tener una lista anidada con ucho indices, para revisar
#cada uno de los elmenots de la lista, usemos tantos bucles for anidados, como
#índices haya, con cuatro índices iterar sobre índices enteros se ve como :

# for i1 in range(len(somelist)):
#     for i2 in range(len(somelist[i1])):
#           for i3 in range(len(somelist[i1][i2])):
#                     for i4 in range(len(somelist[i1][i2][i3])):
#                     value = somelist[i1][i2][i3][i4]
# # work with value

#y la version que itera sobre las sublistas se convierte en:

    
# for sublist1 in somelist:
#     for sublist2 in sublist1:
#         for sublist3 in sublist2:
#             for sublist4 in sublist3:
#                 value = sublist4
# # work with value

#TRABAJANDO CON TUPLAS 

# un ejemplo de tupla es:

t= ( 2, 4, 6, "temp.pdf")

#de la misma forma 

t= 2, 4, 6, "temp.pdf"
for element in "mylife.txt", "yourlife.txt", "herlife.txt":
    print(element,)

#muchas de las opciones en listas también son útilen en tuplas 

t= t + (-1.0, -2.0)
print(t)
print(t[1])
print(t[2:])
print(6 in t)

#no podemos cambiar elemento en las tuplas
#t[1]= -1, t.append(),  del t[1], me da error


#funciones y ramificaciones 

def F(C):
    return (9/5)*C + 32

#para llamar la función 

temp1= F(15.5)
print(temp1)

a= 10
temp2= F(a)
print(temp2)
print(F(a+ 1))
print(F(a + 1) + F(20))

Fgrados= [F(C) for C in Cgrados]
print(Fgrados)

























