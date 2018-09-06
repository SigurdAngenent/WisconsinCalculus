
#!/usr/bin/python
## Time-stamp: Mon Sep  3 14:58:50 CDT 2007 angenent

from  grapher  import *
from math import *

def x(t): return t
def fx(t): return 1-t*(1-t)*6
def dydx(t): return -6*(1-2*t)

def tangentSegment(t, seglen=0.5):
    vx=1
    vy=dydx(t)
    v=sqrt(vx*vx+vy*vy)
    vx, vy= vx/v, vy/v
    xx, yy = x(t), fx(t)
    line([xx- seglen*vx, yy-seglen*vy],\
         [xx+ seglen*vx, yy+seglen*vy])
    roundPoint([xx, yy], 0.03)

setViewBox(-0.1,-0.6, 1.1, 1.1)
openOutputFile("05interiormin",120)


axes()

#the graph
linewidth(2)
plot(x,fx, 0, 1)
line([0,0], [1,0])
linewidth(1)

roundPoint([0, fx(0)], 0.03)
roundPoint([1, fx(1)], 0.03)

tangentSegment(0.5,0.25)
#annotations
closeOutputFile()


