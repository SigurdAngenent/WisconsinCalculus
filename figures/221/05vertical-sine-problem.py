#!/usr/bin/python
# Solution to the right angle problem
from math import *
from grapher import *

def x(t): return sin(t)

def y(t): return t


setViewBox(-1.2,-2.2*pi, 1.2, 2.2*pi)
openOutputFile("05vertical-sine-problem", 48)

axes([5,5])
plot(x, y,-2.1*pi, 2.1*pi)
for t in range(-4, 9):
    line([-0.1,t*pi/2], [0.1,t*pi/2])
annotate([x(0.8*pi),  y(0.8*pi)], [1,1], makeboxl(r"$x=\sin(y)$"))
annotate([0, -2*pi], [-2,1], makeboxr(r"$-2\pi$") )
annotate([0, -1*pi], [2,2], makeboxl(r"$-\pi$") )
annotate([0,  1*pi], [2,2], makeboxl(r"$\pi$") )
annotate([0,  2*pi], [-2,2], makeboxr(r"$2\pi$") )
closeOutputFile()


