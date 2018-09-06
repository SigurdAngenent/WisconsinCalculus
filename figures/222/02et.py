#!/usr/bin/python
# Graph of e^x and first three Taylor polynomials.
from math import *
from grapher import *

def id(t):
    return t
def f(t):
    return exp(t)
def drawparabola(k):
    y=lambda t: 1+t*(1+k*t)
    plot(id, y, -2.4, 1.3)

# set view box, open output file
setViewBox(-2.5, -0.75, 1.6, 4.0)
openOutputFile("02et", 240)

setrgbcolor([128, 128, 128])
a,b = -2.5, 1.3
N=200
dx=(b-a)/N
xvals = [a+k*dx for k in range(N+1)]
expsubgraph = [[x, f(x)] for x in xvals]
expgraph= [p for p in expsubgraph]
expsubgraph.append([b,0])
expsubgraph.append([a,0])
#expsubgraph.append([a, f(a)])
setrgbcolor('chartreuse4')
polygonF(expsubgraph, 'chartreuse')
setrgbcolor([0,128,0])
polygonA(expgraph)

setrgbcolor('black')
arrow([0, -0.25], [0, Viewymax()-0.1], len=7, wid=2)
arrow([Viewxmin(), 0], [Viewxmax()-0.1,0], len=7, wid=2)

linewidth(0.5)
drawparabola(-0.5)
drawparabola(0.0)
drawparabola(1.0)
drawparabola(1.5)
setrgbcolor('red')
linewidth(1.0)
drawparabola(0.5)


annotate([-1.6, -0.6], [-6,0], rotatebox(45, r"$y=1+x$"))
annotate([-2.5, exp(-2.5)], [0, 3], rotatebox(5, r"$y=e^x$"))
annotate([-2.5, 1-2.5*(1-0.5*2.5)], [0, 0], makeboxc(r"$y=1+x+\frac12x^2$"))
annotate([-2.0, 1-2.0*(1-1.0*2.0)], [-3, 0], makeboxr(r"$y=1+x+x^2$"))
annotate([-1.3, 1-1.3*(1-1.5*1.3)], [3, 0], makeboxl(r"$y=1+x+\frac32x^2$"))
annotate([-1.1, 1-1.1*(1+0.5*1.1)], [3, 0], makeboxl(r"$y=1+x-\frac12x^2$"))

closeOutputFile()


