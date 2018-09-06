#!/usr/bin/python
# Time-stamp : Sunday, November 18, 2007 4:14:28 PM
from  grapher  import *
from math import *
from random import random


def f(t): return 1/(1+(2*t-1)**2)

setViewBox(-0.3,-0.1,2.3,1.1)
openOutputFile("08AreaUnderGraph",150)

a=0.0
b=2.0
c=(a+b)/2
n=200
dx=(b-a)/200
frame=[a+i*dx for i in range(n+1)]
frame = [(x, f(x)) for  x in frame]
frame.append((b, 0))
frame.append((a, 0))

setrgbcolor ([200,200,200])
polygonF(frame)
setrgbcolor('black')
linewidth(2)
polygonC(frame)

linewidth(1)
x_axis(5)
plot(lambda x:x, f, Viewxmin(), Viewxmax())



#boundary of region
setlinecap(1)
setrgbcolor('blue')
#linewidth(2)



annotate([a,0], [-2, -12], "$a$")
annotate([b,0], [-2, -12], "$b$")
annotate([c, f(c)] , [3, 3], "$y=f(x)$")

closeOutputFile()


