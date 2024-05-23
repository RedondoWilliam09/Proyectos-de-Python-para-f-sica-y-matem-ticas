
#4.1 hacer preguntas y leer respuestas 

    #siguiendo con nuestro ejemplo tenemos:
    
# C= input("C=  ")
# C= float(C)
# F= (9/5)*C + 32
# print(F)

#podemos mejorar tal que aparerezcan los argumento con el nombre del programa en
#la terminal


# import sys
# #C= input("C=  ")
# C = float(sys.argv[1])
# F = (9.0/5)*C + 32
# print(F)
# help(sys)

import sys
t = float(sys.argv[1])
v0 = float(sys.argv[2])
g = 9.81
y = v0*t - 0.5*g*t**2
print(y)

#necesito ver por qué sale eror para lineas de comandos 













