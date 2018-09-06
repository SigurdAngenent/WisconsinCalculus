#!/usr/bin/python
## Time-stamp : Thursday, September 6, 2007 2:32:42 PM
from grapher import *
from math import *

# Let's solve 2y+sin y = pi/2
a, b = 0, pi
while (b-a)>1e-8:
    c = (a+b)/2
    x = 2*c + sin(c)
    if x>pi:
        b=c
    else: a=c
    print "%15.10lf  %15.10lf"%(a,b)
c=(a+b)/2

setViewBox(-0.5*pi,-0.5*pi, 3.1*pi, 2.1*pi)
openOutputFile("04ImplicitFunctionExample",90)

#the drawing
axes([5,5])
plot((lambda y: 2*y+sin(y)), (lambda y:y), -3*pi, 3*pi)

linewidth(0.2)
setrgbcolor('aqua')
for j in range(-2, 3):
    line([-3*pi, j*pi], [3*pi, j*pi])
    line([j*pi, -3*pi], [j*pi, 3*pi])

linewidth(1)
setrgbcolor('red')
line([1.25*pi,0.25*pi], [2.75*pi, 1.75*pi])
setrgbcolor('black')
linewidth(0.5)
roundPoint([2*pi, pi], 0.2)
roundPoint([pi, c], 0.2)
roundPoint([0,0], 0.2)
annotate([pi, 0], [0, -6], 
         makeboxc(r"\footnotesize$\pi$") )
annotate([2*pi, 0], [0, -6], 
         makeboxc(r"\footnotesize$2\pi$") )
annotate([0, pi], [2, 1], 
         makeboxl(r"\footnotesize$\pi$") )

closeOutputFile()
    

