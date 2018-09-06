#!/usr/bin/python
## Time-stamp: <Thursday May 03 2012 20:09:31>

from grapher import *
from math import *

def segment(a,b):
    plot(lambda t:t, lambda t:sin(t), a, b)

setViewBox(-5.0,-1.5, 5.0,1.5)
openOutputFile("01sine",180)

axes([5,5])
linewidth(2)
setrgbcolor('blue')
segment(-pi/2, pi/2)
setrgbcolor('black')
linewidth(0.3)
setdash("[1 1]0")
segment(-4.5, -pi/2)
segment(pi/2, 4.5)
linewidth(0.5)
polygonA([(pi/2, 0), (pi/2, 1), (0, 1)])
polygonA([(-pi/2, 0), (-pi/2, -1), (0, -1)])
setdash("[] 0")
roundPoint([pi/2, 0], 0.04)
roundPoint([pi/2, 1], 0.04)
roundPoint([-pi/2, 0], 0.04)
roundPoint([-pi/2, -1], 0.04)
roundPoint([0, 1], 0.04)
roundPoint([0, -1], 0.04)

annotate([pi/2, 0], [2, 4], "$\pi/2$")
annotate([-pi/2, 0], [0, 4], makeboxc("$-\pi/2$"))
annotate([0, 1], [-8,0], makeboxr("$1$"))
annotate([0, -1], [3,0], makeboxl("$-1$"))
annotate([pi/2, -1], [0,0], makeboxl("$y=\sin x$"))
closeOutputFile()




