#!/usr/bin/python
## Time-stamp: Tue Sep  4 14:42:31 CDT 2007 angenent

from  grapher  import *
from math import *

def x(t): return t
def f(t): return 0.5*t+t*t*sin(pi/t)
def g(t): return t*(0.5+t)
def h(t): return t*(0.5-t)

setViewBox(-0.6,-0.6, 0.6, 0.6)
openOutputFile("05zigzagBetweenParabolas",210)

axes()

#tangent at origin
linewidth(0.5)
line([-0.6,-0.3], [0.6, 0.3])
linewidth(1)
#upper and lower parabolas
setdash("[2] 0")
setrgbcolor([0,128,0])
plot(x,g, -0.6, 0.6)
plot(x,h, -0.6, 0.6)
setdash("[] 0")
#the graph of f
setrgbcolor([0,0,128])
plot(x,f, -0.6, -0.001)
plot(x,f, 0.001, 0.6)
setrgbcolor('black')

for k in range(2,10):
    roundPoint([1.0/k, 0.5/k], 0.04/(k+2))

#annotations
annotate([0.5, g(0.5)], [4,0],"$y=\\frac 12x+x^2$")
annotate([-0.5, h(-0.5)], [4,0],"$y=\\frac 12x-x^2$")
annotate([0.6, 0.3], [3,0], "$y=\\frac 12x$")
annotate([0.55, f(0.55)], [2, 2], "$y=\\frac 12x+x^2\\sin\\frac\\pi x$")
closeOutputFile()


