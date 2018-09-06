#!/usr/bin/python
## Time-stamp: <2012-07-06 11:14:05 angenent>

from  grapher  import *
from math import *

def x(t): return t
def fx(t): return t*t


setViewBox(-1,-1, 1,1)
openOutputFile("05parabola",150)
axes()

#the graph
setrgbcolor([255, 0, 0])
plot(x,fx, -1, 0)
setrgbcolor([0,0,  255])
plot(x,fx, 0, 1)
setrgbcolor([0, 0, 0])

#annotations
annotate([-0.7, 0.8], [0,0], "$f'(x)<0$")
annotate([0.2, 0.8], [0,0], "$f'(x)>0$")

closeOutputFile()


