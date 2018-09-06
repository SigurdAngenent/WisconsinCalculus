#! /usr/bin/python

from grapher import *
from math import *

def x(t):  return (t)
def fx(t): return t*cos(pi/t)

setViewBox(-1.3,-1.4,1.3,1.4)
openOutputFile("03backwardCosSandwichSmall",90)

axes([5,5])

linewidth(0.2)
setrgbcolor('ocean')

tmax=1.0
for k in range(5):
    plot(x,fx, tmax/4, tmax)
    plot(x,fx, -tmax/4, -tmax)
    tmax/=4

setrgbcolor('black')
linewidth(1)
roundPoint([0,0], 0.05)
linewidth(0.2)
arrow([-0.6, -1.4], [-0.05, -0.1], 7, 2)
txt = r"""\parbox{90pt}{\footnotesize\centering%
removable discontinuity,\\
or, a hole in the graph}"""
annotate([-1.3, -1.4], [0, -12], txt)
annotate([x(-1), fx(-1)], [-12,4], r"\footnotesize$y=x\cos\dfrac\pi x$")
closeOutputFile()


