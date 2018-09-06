
#!/usr/bin/python
## Time-stamp: Mon Sep  3 07:32:49 CDT 2007 angenent

from  grapher  import *
from math import *

def x(t): return t
def fx(t): return t*(t*t-1)

def tangentSegment(t, seglen=0.5):
    vx=1
    vy=3*t*t-1
    v=sqrt(vx*vx+vy*vy)
    vx, vy= vx/v, vy/v
    xx, yy = x(t), fx(t)
    line([xx- seglen*vx, yy-seglen*vy],\
         [xx+ seglen*vx, yy+seglen*vy])
    roundPoint([xx, yy], 0.03)

setViewBox(-2.0,-1.5, 2.0,1.5)
openOutputFile("05cubicBegin",120)

a=sqrt(1.0/3.0)
axes()




tangentSegment(a)
tangentSegment(-a)
#annotations
annotate([0.0, 1.5], [3, 0], "$y$")
annotate([2.0, 0.0], [2, -2], "$x$")
closeOutputFile()


