#!/usr/bin/python
## Time-stamp: <2012-07-25 10:08:17 angenent>

from grapher  import *
from math import *
from random import *

def x(t): return t
def fx(t): return 1/(1+(2*t-1)**2)


setViewBox(-0.3,-0.1,2.3,1.1)
openOutputFile("08Riemann-fine", 150)

n=20
dx=2.0/n
xp = [i*dx for i in range(n+1)]

c=[(uniform(xp[i],xp[i+1]) + xp[i] + xp[i+1])/3 for i in range(n)]
for i in range(n):
    polygonF(rect(xp[i]+0.05*dx, xp[i+1]-0.05*dx, 0, fx(c[i])), [128,128,128])
    polygonC(rect(xp[i], xp[i+1], 0, fx(c[i])) )

plot(x, fx, Viewxmin(), xp[0])
plot(x, fx, xp[n], Viewxmax())
setrgbcolor('blue')
plot(x, fx,  xp[0], xp[n])
for x in (xp[0], xp[n]):
    line([x,0], [x, fx(x)])
line([xp[0],0], [xp[n],0])
setrgbcolor('black')
linewidth(1)
x_axis(5)

annotate([xp[0], 0], [-1, -14], "$a$")
annotate([xp[n], 0], [-2, -14], "$b$")



closeOutputFile()


