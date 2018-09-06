#!/usr/bin/python
## Time-stamp: <2007-11-09 22:28:35 angenent>

from grapher  import *
from math import *
from random import *

def x(t): return t
def fx(t): return 1/(1+2*t*t)


setViewBox(-0.3,-0.1,2.3,1.1)
openOutputFile("04Riemann1D-fine", 150)

n=30
dx=2.0/n
xp = [i*dx for i in range(n+1)]

c=[(uniform(xp[i],xp[i+1]) + xp[i] + xp[i+1])/3 for i in range(n)]

plot(x, fx, Viewxmin(), xp[0])
plot(x, fx, xp[n], Viewxmax())

#setrgbcolor('blue')
#linewidth(2)
plot(x, fx,  xp[0], xp[n])
for x in (xp[0], xp[n]):
    line([x,0], [x, fx(x)])
line([xp[0],0], [xp[n],0])
#setrgbcolor('black')
#linewidth(1)
x_axis()

linewidth(0.5)
annotate([xp[0], 0], [-1, -14], "$a$")
for i in range(n):
    y = fx(c[i])
    polygonC([[xp[i], 0], [xp[i+1], 0], [xp[i+1], y], [xp[i], y]])

annotate([xp[n], 0], [-2, -14], "$b$")



closeOutputFile()


