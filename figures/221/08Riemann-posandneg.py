#!/usr/bin/python
# Time-stamp : Sunday, November 18, 2007 4:29:43 PM
from grapher  import *
from math import *
from random import *

def x(t): return t
def fx(t): return cos(t)


setViewBox(-0.3,-1.0,3.4,1.1)
openOutputFile("08Riemann-posandneg",240)

n=30
dx=3.0/n
xp = [i*dx for i in range(n+1)]
fxp = [fx(xx) for xx in xp]
c=[(uniform(xp[i],xp[i+1]) + xp[i] + xp[i+1])/3 for i in range(n)]
R=[rect(xp[i], xp[i+1], 0, fx(c[i])) for i in range(n)]

plot(x, fx, Viewxmin(), xp[0])
plot(x, fx, xp[n], Viewxmax())

#draw the box fills
for i in range(n):
    if fxp[i]<0 :
        polygonF(R[i], 'gray')

#draw the boundary of the region
setrgbcolor('blue')
linewidth(2)
plot(x, fx,  xp[0], xp[n])
for x in (xp[0], xp[n]):
    line([x,0], [x, fx(x)])
line([xp[0],0], [xp[n],0])
setrgbcolor('black')
x_axis(5)

#draw the boxes
linewidth(0.5)
for i in range(n):
    polygonC(R[i])



annotate([xp[0], 0], [-1, -12], "$a$")
annotate([xp[n], 0], [-2, 4], "$b$")



closeOutputFile()


