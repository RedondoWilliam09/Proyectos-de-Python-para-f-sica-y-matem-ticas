#pares de opción valor en la línea de comandos 

#uso del módulo argparse

#primero debemos crear un objeto analizador 
s0=v0=0; a=t=1
import argparse
parser = argparse.ArgumentParser()

#necesitamos definir varias opciones en la línea de comandos 

parser.add_argument('--v0','--initial_velocity', type=float, default=0.0, 
                    help='initial velocity', metavar='v')
parser.add_argument('--s0','--initial_position',type=float,
                    default= 0.0, help= 'initial position', metavar= 's' )
parser.add_argument('--a','--aceleration',type= float, default= 1.0,
                    help= 'aceleration', metavar= 'a')
parser.add_argument('--t','--time', type=float,
                    default=1.0, help= 'time', metavar= 't' )

#ahora debemos leer los argumentos  en la línea de comandos 

args= parser.parse_args()

#ahora podemos extraer el valor de varios parámetros registrados 

# #parser.add_argument('--initial_velocity','--v0', type=float,
#                     default=0.0, help= 'initial velocity')

#hará que el valor de velocidad inicial aparezca como args.initial_velocity 

#podemos agregar la palabra clave desk para especificar el nombre donde se almacena
#el valor

# #parser.add_argument('--initial_velocity','--v0', dest='v0',
#                     type=float, default=0, help= 'initial velocity')

#ahora, arg.v0  recuperará el valor de la velocidad inicial, en caso de que no proporcione
#ningúnvalor predeterminado, el valor será ninguno, nuestro ejemplo se completa evaluando s como:

#s= args.s0 + args.v0*t + 0.5*args.a*args.t**2

#o introduciendo nuevas variables para que la fórmuloa se alinee a su notacion matemática 

s0= args.s0; v0=args.v0; a= args.a; t=args.t 
s= s0 + v0*t + 0.5*a*t**2

print("un objeto que comienza en s= %g a t = 0 con velocidad inicial %s m/s, y sujeto a una aceleraciónconstante %g m/s**2 se encuentra en la posición s= %g m despues de %s segundos." %(s0,v0,a,s,t))




















