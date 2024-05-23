# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 12:41:58 2022

@author: william
"""

# la clase polinomio utilizando la adción de objetos toma la forma...

class Polynomial(object):
    def __init__(self, coefficients):
        self.coeff = coefficients
    
    def __call__(self, x):
        """
        evaluamos el polinomio

      
        """
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s
    
    def __add__(self, other):
        
        """nos regresa el self mas otro polinomio como objeto"""
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:] #copiamos todos los elemntos en self.coeff
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        
        else:
            result_coeff = other.coeff[:] #copiamos todos los elementos en other.coeff
            for i in range(len(self.coeff)):
                result_coeff[i] +=self.coeff[i]
        
        return Polynomial(result_coeff)
    
    #podemos crear una clase para multimplicar dos polimonios de la forma...

    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        import numpy as np
        result_coeff = np.zeros(M + N + 1)
        for i in range(0, M+1):
            for j in range(0, N + 1):
                result_coeff[i + j] += c[i]*d[j]
        return Polynomial(result_coeff)
    
    #podemos implementar un metodo para diferenciar el polinomio resultante 
    #podemos construir dos enfoques 
    
    def differentiate(self):
        """deriva el polinomio en el mismo lugar"""
        for i in range(1, len(self.coeff)):
            self.coeff[i-1] = i*self.coeff[i]
        del self.coeff[-1]
    
    def derivative(self):
        """copiar el polinomio y regresar su derivada"""
        dpdx = Polynomial(self.coeff[:]) #hacemos una copia
        dpdx.differentiate()
        return dpdx 
    
    # def __str__(self):
    #     s = ''
    #     for i in range(len(self.coeff)):
    #         s += ' + %g*x^%d' % (self.coeff[i], i)
    #     return s
            
    # podemos contruir un médo de ipresión mejorado de la forma...
    
    def __str__(self):
        s = ''
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], i)
        
        # para corregir diseño hacemos...
        
        s = s.replace('+ -', '- ')
        s = s.replace('x^0','1')
        s = s.replace(' 1*',' ')
        s = s.replace('x^1','x ')
        if s[0:3] == ' + ':
            s = s[3:]
        if s[0:3] == ' - ':
            s = '-' + s[3:]
        return s
    
    
        
        
        
# una implementación de la clase polinomio va de la forma...

#pag 446 libro guía

p1 = Polynomial([1, -1])
p2 = Polynomial([0, 1, 0, 0, -6, -1])
p3 = p1 + p2
print(p3.coeff)

p4 = p1*p2
print(p4.coeff)
p5 =p2.derivative()
print(p5.coeff)
print(p1.coeff)
print(p2.coeff)

#para  los polinomios podemos hacer-..
x = 0.5
y = 2
p1_mas_p2 = p1(x) + p2(x)
p1_mas_p22 = p1(y) + p2(y)
print(p1_mas_p2)
print(p1_mas_p22)               
            
p3_value = p3(x)
print(p1_mas_p2 - p3_value)

print(p3)

p4 = p3.derivative()
print(p4)

#podemos implementar una función de prueba para la clase polinomio, utilizando la convención que venimos utilizando 
#la función de priueba toma la forma...

def tes_polynomial():
    p1 = Polynomial([1- -1])
    p2 = Polynomial([0, 1, 0, 0, -6, -1])
    p3 = p1 + p2
    p3_exact = Polynomial([1, 0, 0, 0, -6, -1])
    assert p3.coeff == p3_exact.coeff
    
    p4 = p1*p2
    import numpy as np
    p4_exact = Polynomial(np.array([0, 1, -1, 0, -6, 5, 1]))
    assert np.allclose(p4.coeff, p4_exact.coeff, rtol = 1E-14)
    
    p5 = p2.derivative()
    p5_exact = Polynomial([1, 0, 0, -24, -5])
    assert p5.coeff == p5_exact.coeff
    
    p6 = Polynomial([0, 1, 0, 0, -6, -1]) #p2
    p6.differenciate()
    p6_exact = p5_exact 
    assert p6.coeff == p6_exact.coeff
    


    
    
    
    
    
    
    
    
    












        