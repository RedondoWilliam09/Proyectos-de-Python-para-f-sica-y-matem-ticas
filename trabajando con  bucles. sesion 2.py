
print("-----------------------------")
c=-20
dc=5
while c<=40:
    F = (9/5)*c +32
    print(c, F)
    c=c+dc
print("-----------------------------")


from pylab import *

x = linspace(-3, 3, 50)
y= x - (x - 1)*sin(x)
plot(x,y)
