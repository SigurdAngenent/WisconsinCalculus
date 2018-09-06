#!/usr/bin/python
from math import *
from grapher import *

def id(t): return t
def f(t): return 1.0/(1+t*t)
def T(n): 
    return (lambda t: (1-(-t*t)**(n+1))/(1+t*t))

setViewBox(-3.1, -0.75, 3.1, 2.0)
openOutputFile("02AgnesiSeries", 360)

setrgbcolor([200, 255, 200])
a,b = -3.0, 3.0
N=200
dx=(b-a)/N
xvals = [a+k*dx for k in range(N+1)]
geoseriessubgraph = [[x, f(x)] for x in xvals]
geoseriessubgraph.append([b,0])
geoseriessubgraph.append([a,0])
geoseriessubgraph.append([a, f(a)])
polygonF(geoseriessubgraph)

setrgbcolor('black')
line([a,1], [b,1])

setrgbcolor('black')
lw=0.7
for n in range(1,40):
    lw*=0.8
    linewidth(lw)
    plot((lambda t:t), T(n), -1.1, 1.1)

x=-3.0
while(x<3.05):
    line([x,0], [x, -0.03])
    x+=0.1
for x in [-1, -0.5, 0.5, 1]:
    line([x,0], [x, -0.06])
linewidth (0.5)
axes()

closeOutputFile()

