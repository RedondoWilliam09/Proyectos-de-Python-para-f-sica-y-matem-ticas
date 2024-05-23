

#ejercicio 7.8  

# ajuste de funciones en una clase 
# El propósito de este ejercicio es crear una interfaz de clase para un 
# conjunto de funciones ya existente implementando el método de
#  interpolación de lagrange 

# la clase debe incluir un método de trazado para x entre el primer y 
# último punto de interpolación, además de escribir la clase en sí, debe escribir 
# el código para verificar la implementación 


class LagrangeInterpolation(object):
    """es conveniente definir la entrad a la funcion
    a interpolar con un array en num,py"""
    
    def __init__(self, l_i, l_s, c_ls, yp):
        self.l_i, self.l_s, self.c_ls, self.yp = l_i, l_s, c_ls, yp
         
    def FInterpolation(self, n):
        l_i, l_s, c_ls, yp =  self.l_i, self.l_s, self.c_ls, self.yp
        self.n = n
        import numpy as np
        import copy
        from matplotlib.pylab import plot, show
        xp= np.linspace(l_i,l_s,c_ls)
        xp2 =copy.copy(xp)
        
        
        
        print(xp2)
        F = np.ones(n+1) 
        G= np.zeros(len(xp))
        x = np.ones(n+1)
        for i in range(len(x)):
            x[i] = round(np.random.uniform(l_i, l_s),2)
            
        for i in range(len(x)):
            for j in range(len(x)):
                if i != j:
                    while (x[i]==x[j]):
                        x[j] = round(np.random.uniform(l_i, l_s),2)
        
       
        for k in range(len(xp)):
            for i in range(n+1):
                for j in range(n+1):
                    if x[i] != x[j]:
                        c = x[i]- x[j]
                        if c != 0:
                            
                            dl = (((xp2[k] - x[j])/c))
                            F[i] *= dl
                xp = x 
                F[i] = F[i]*yp[i]
                G[k] += F[i]
                xp = xp2
            F = np.ones(n+1) 
        print(G)
        plot(xp2, G)
        
        show()
        return G

    def comparison(self):
        import numpy as np
        
        l_i, l_s, c_ls, yp =  self.l_i, self.l_s, self.c_ls, self.yp
        
        xp= np.linspace(l_i,l_s,c_ls)
        p = self.FInterpolation(self.n)
        from matplotlib.pylab import plot, show
        plot(xp, yp)
        plot(xp, p)
        show()

import numpy as np
xp = np.linspace(-2*np.pi, 2*np.pi, 60)
yp = np.sin(xp)
p_1= LagrangeInterpolation(-2*np.pi, 2*np.pi, 20, yp)
p_1.FInterpolation(4)
# p_1.comparison()


        
        
        
                
                
                
                
            
        
            
            
            
            
        

























