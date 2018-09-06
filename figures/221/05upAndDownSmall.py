from grapher import *
from math import *

def x(t): return t
def fx(t): return t*(t*t-3)
def tangentSegment(t, seglen=0.5):
    vx=1
    vy=3*t*t-3
    v=sqrt(vx*vx+vy*vy)
    vx, vy= vx/v, vy/v
    xx, yy = x(t), fx(t)
    line([xx- seglen*vx, yy-seglen*vy],\
         [xx+ seglen*vx, yy+seglen*vy])
    roundPoint([xx, yy], 0.1)

setViewBox(-4, -4, 4, 4)
openOutputFile("05upAndDownSmall",72)

a=1.0

axes([4,4])

#the graph

plot(x,fx, -3, 3)

linewidth(0.25)
for t in (-a, a):
    setdash("[1 1] 0")
    line([t, 0], [t, fx(t)])
    setdash("[] 0")
    roundPoint([t, 0], 0.1)
    tangentSegment(t, seglen=0.5)
annotate([a, 0], [0, 2], makeboxc(r"{\ttfamily\upshape1}"))
annotate([-a, 0], [0, -8], makeboxc(r"{\ttfamily\upshape-1}"))
annotate([0, Viewymin()], [0, -10], makeboxc(r"$y=x^3-3x$"))

#regions
linewidth(0.5)

#annotations

closeOutputFile()


