

# función eval magic

import sys

r = eval("1+2")
print(r)

print(type(r))

r = eval("2.5")
print(r)
print(type(r))


r = eval("[1, 6, 7.5]")
print(r)
print(type(r))

r = eval("(-1, 1)")
print(r)
print(type(r))


# de la misma forma


r = eval("sqrt(2)")
print(r)
print(type(r))

# eval me convierte una cadena de string en un formato de acuerdo al contenido pueden ser listas, float o int o tuplas
# que es el equivalente a convertir a codigo phyton una cadena string

# también tenemos:

r = eval('"math programming"')
print(r)
print(type(r))

# sobre incluir cadenas en phyton

# si hacemos

# r= math programming
# phyton lo tomará como error
# pero si hacemos:


i1= eval(input("dato de entrada 1="))
i2= eval(input("dato de entrada 2="))
r= i1 + i2
print("%s + %s se convierte %s \n with value %s " %(type(i1), type(i2), type(r), r))

#LA FUNCIUÓN EVAL ES ÚTIL PARA INCLUIR FÓRMULAS 
formula= input("inserta la fórmula= ")
x= eval(input("inserta el valor de x= "))
result= eval(formula)
print("%s for x= %s se mantiene %g" %(formula, x, result))









