# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 15:26:10 2022

@author: william
"""


# 1. clase para rectangulo 

class rectangle(object):
    def __init__(self, x0, y0, x1, y1, x2, y2, x3, y3 ):
        self.x0, self.y0, self.x1, self.y1, self.x2, self.y2, self.x3, self.y3  \
        = x0, y0, x1, y1, x2, y2, x3, y3
    
    def Area(self):
        x0, y0, x1, y1, x2, y2 = \
        self.x0, self.y0, self.x1, self.y1, self.x2, self.y2, 
        import numpy as np
        w = np.sqrt((x1 - x0)**2 + (y1 - y0)**2)
        h = np.sqrt((x2 - x0)**2 + (y2 - y0)**2)
        a = w*h
        return a
    def Perimeter(self):
        x0, y0, x1, y1, x2, y2 = \
        self.x0, self.y0, self.x1, self.y1, self.x2, self.y2, 
        import numpy as np
        w = 2*np.sqrt((x1 - x0)**2 + (y1 - y0)**2)
        h = 2*np.sqrt((x2 - x0)**2 + (y2 - y0)**2)
        b = w + h
        return b

rectangulo_1 = rectangle(0, 0, 2, 0, 0, 2, 2, 2)
print(rectangulo_1.Area())
print(rectangulo_1.Perimeter())

# 2. clase para un triangulo generalizado 

class Triangle(object):
    def __init__(self,x1, y1, x2, y2, x3, y3  ):
        self.x1, self.y1, self.x2, self.y2, self.x3, self.y3  \
        =  x1, y1, x2, y2, x3, y3
    
    def Area(self):
        x1, y1, x2, y2, x3, y3 = self.x1, self.y1, self.x2, self.y2, self.x3, self.y3
        a = (1/2)*(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)
        return a
    
    def Perimeter(self):
        x1, y1, x2, y2, x3, y3 = self.x1, self.y1, self.x2, self.y2, self.x3, self.y3
        import numpy as np
        p = np.sqrt((x2 - x1)**2 + (y2 - y1)**2) + np.sqrt((x3 - x2)**2 + (y3 - y2)**2) \
            + np.sqrt((x3 - x1)**2 + (y3 - y1)**2)
        return p

triangulo_1 =Triangle(0, 0, 4, 0, 2, 4)
print(triangulo_1.Area())
print('el perimetro me da:', triangulo_1.Perimeter())
import numpy as np
p_exact = 2*np.sqrt(20) + 4
print(p_exact)


# necesitamos contruir una función test para cada una de las clases 
# implementadas 

def test_Triangle():
    import numpy as np
    triangulo_1 =Triangle(0, 0, 4, 0, 2, 4)
    area_exact = (1/2)*(4)*(4)
    area_computed = triangulo_1.Area()
    exact_perimeter = 2*np.sqrt(20) + 4
    perimeter_computed = triangulo_1.Perimeter()
    diff = abs(area_exact - area_computed)
    tol = 1E-15
    assert diff < tol, 'bug en la clase triangle, diff =%s' % diff
    diff2 = abs(exact_perimeter - perimeter_computed)
    assert diff2 < tol, 'bug en la clase triangle, diff =%s' % diff2
    

def test_rectangle():
    rectangulo_1 = rectangle(0, 0, 2, 0, 0, 2, 2, 2)
    area_exact = 2*2
    area_computed = rectangulo_1.Area()
    exact_perimeter = 2*area_exact
    perimeter_computed = rectangulo_1.Perimeter()
    diff = abs(area_exact - area_computed)
    tol = 1E-15
    assert diff < tol, 'bug en la clase rectangle, diff =%s' % diff
    diff2 = abs(exact_perimeter - perimeter_computed)
    assert diff2 < tol, 'bug en la clase rectangle, diff =%s' % diff2



        


    
test_Triangle()
        
        

