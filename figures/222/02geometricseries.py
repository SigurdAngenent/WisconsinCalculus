#!/usr/bin/python
from math import *
from grapher import *

def id(t): return t
def f(t): return 1.0/(1-t)
def T(n): 
    return (lambda t: (1-t**(n+1))/(1-t))

setViewBox(-1.25, -0.75, 1.2, 4.1)
openOutputFile("02geometricseries", 240)

setrgbcolor( 'navajowhite' )
a,b = -1.24, 0.75
N=200
dx=(b-a)/N
xvals = [a+k*dx for k in range(N+1)]
geoseriessubgraph = [[x, f(x)] for x in xvals]
geoseriessubgraph.append([b,0])
geoseriessubgraph.append([a,0])
geoseriessubgraph.append([a, f(a)])
polygonF(geoseriessubgraph)

setrgbcolor('black')
lw=0.7
for n in range(40):
    lw*=0.9
    linewidth(lw)
    plot((lambda t:t), T(n), -1.1, 0.7)

x=-1.0
while(x<1.05):
    line([x,0], [x, -0.03])
    x+=0.1
for x in [-1, -0.5, 0.5, 1]:
    line([x,0], [x, -0.06])
linewidth (0.5)
axes()
setdash ("[4 4] 0")
line([1.0, -0.7], [1.0, 3.3])

closeOutputFile()


