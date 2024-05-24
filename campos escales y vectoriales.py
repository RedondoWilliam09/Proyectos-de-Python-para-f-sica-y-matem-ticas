


""""
Imlementando campos escalares y vectoriales usando python.

________________________________
"""


import numpy as np

import matplotlib.pyplot as plt

x2=y2=np.linspace(-10,10,100)

#xv, yv = np.linspace(x,y, indexing= 'ij', sparce= False)


xv, yv = np.meshgrid(x2, y2, indexing = 'ij', sparse = False)

ho= 2277
R=4


hv=ho/(1 + (xv**2 + yv**2)/(R**2))


#el vector gradiente del campo h(x,y) va como:
    

dhdx, dhdy = np.gradient(hv)

# fig= plt.figure(1)   #obtengo la figura 
# ax= fig.gca()   #obtener ejes

#para visualizacion en 3 dimensiones necesitamos de las siguientes herramientas




#parámetros de la curva parametrizada

s= np.linspace(0, 2*np.pi, 1000)

curve_x = 10*(1- s/(2*np.pi))*np.cos(s)
curve_y = 10*(1- s/(2*np.pi))*np.sin(s)
curve_z= ho/(1 + 100*(1 - s/(2*np.pi))**2/(R**2))


from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(1)

ax= fig.gca(projection ='3d')
ax.plot_wireframe(xv,yv,hv, rstride= 2, cstride= 2)

#gráfica simple de montaña y curva paramétrica 

fig= plt.figure(2)
ax= fig.gca(projection= '3d')


from matplotlib import cm

ax.plot_surface(xv,yv, hv, cmap=cm.coolwarm, rstride= 1, cstride=1)

#agregar la curva paramétrica, linewidth controla el ancho de la curva 

ax.plot(curve_x, curve_y, curve_z, linewidth= 10)
#plt.show()


#graficación de gráficos de contorno:
 
#gráfico de contorno predeterminado con 7 líneas de contorno

fig= plt.figure(3)
ax= fig.gca()
ax.contour(xv,yv,hv)
plt.axis('equal')


#trazado de contorno tridimensional 

fig= plt.figure(4)
ax= fig.gca(projection='3d')
ax.contour(xv,yv,hv)

#trazado de curvas de nivel y montañas proyectadas en los planos de coordenadas 

fig = plt.figure(5)

ax= fig.gca(projection= '3d')
ax.plot_surface(xv,yv,hv, cmap= cm.coolwarm, rstride= 1, cstride=1)
#.show()

ax.contour(xv,yv,hv, zdir= 'z', offset= -1000, cmap=cm.coolwarm)
ax.contour(xv,yv,hv, zdir= 'x', offset=-10, cmap=cm.coolwarm)
ax.contour(xv,yv,hv, zdir= 'y', offset=10, cmap=cm.coolwarm)

#mostrar los contornos como una imagen=

fig= plt.figure(6)
ax= fig.gca()
ax.imshow(hv)  #imagen del contorno del campo escalr hv


# 10 contour lines (equally spaced contour levels)
fig = plt.figure(7)
ax = fig.gca()
ax.contour(xv, yv, hv, 10)
plt.axis('equal')


# 10 black (’k’) contour lines  #10 lineas de contorno negras
fig = plt.figure(8)
ax = fig.gca()
ax.contour(xv, yv, hv, 10, colors='k')
plt.axis('equal')


#especificando los niveles de contorno explicitamente como una lista 

fig=plt.figure(9)
ax= fig.gca()
levels= [500, 1000, 1500, 2000]

ax.contour(xv,yv,hv,levels=levels)
plt.axis('equal')


#agregar etiquetas con el nivel de contorno para cada línea de contorno 

fig= plt.figure(10)
ax= fig.gca()
cs= ax.contour(xv,yv,hv)
plt.clabel(cs)
plt.axis('equal')

#gráfico del campo vectorial 

fig= plt.figure(11)
ax= fig.gca()
ax.quiver(xv,yv,dhdx,dhdy,color='r', angles= 'xy', scale_units= 'xy')

ax.contour(xv,yv,hv)
plt.axis('equal')


#import mayavi.mlab as plt

#☺Create a figure with white background and black foreground

plt.figure(1, fgcolor=(0,0, 0), bgcolor=(1, 1, 1))
# ’representation’ sets type of plot, here a wireframe plot
plt.surf(xv, yv, hv, extent=(0,1,0,1,0,1), representation='wireframe')
# # Decorate axes (nb_labels is the number of labels used
# # in each direction)
plt.axes(xlabel='x', ylabel='y', zlabel='z', nb_labels=5,
color=(0, 0, 0))
# # Decorate the plot with a title
plt.title('h(x,y)', size=0.4)
# # Simple plot of mountain and parametric curve.
# plt.figure(2, fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))
# # # Here, representation has default: colored surface elements
# plt.surf(xv, yv, hv, extent=(0,1,0,1,0,1))
# # # Add the parametric curve. tube_radius is the width of the
# # # curve (use ’extent’ for auto-scaling)
# plt.plot3d(curve_x, curve_y, curve_z, tube_radius=0.2,
# extent=(0,1,0,1,0,1))
# plt.figure(3, fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))
# # # Use ’warp_scale’ for vertical scaling
# plt.surf(xv, yv, hv, warp_scale=0.01, color=(5, 5, 5))
# plt.plot3d(curve_x, curve_y, 2*curve_z, tube_radius=2)


plt.figure(16, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
s = plt.surf(xv, yv, hv, warp_scale=0.01)
for i in range(10):
    # s.mlab_source.scalars is a handle for the values of the surface,
    # and is updated here
    s.mlab_source.scalars = hv*0.1*(i+1)
    plt.savefig('campos_escalares_y_vectoriales%04d.png' % i)
    show()



