#!/usr/bin/python
## Time-stamp: Thu May 29 11:46:43 CDT 2008 angenent

from grapher import *
from math import *

def x(t): return t
def fx(t): return t*(t*t-1)

a=-0.3
sqD=sqrt(4-3*a*a)
b=(-a+sqD)/2
c=(-a-sqD)/2
d=0.6

setViewBox(-2.0,-1.5, 5.0,1.5)
openOutputFile("01cubicANDcircle", 240)

#axes for the cubic
line([-2.0, 0], [2.0,0])
line([0, -1], [0, 1.5])
arrowhead([-2.0, 0], [2.0,0], 5,1,-0.5)
arrowhead([0, -1], [0, 1.5], 5,1,-0.5)

#axes for the circle
line([2.5, 0], [5.0,0])
line([3.75, -1.5], [3.75, 1.5])
arrowhead([3.0, 0], [5.0,0], 5,1,-0.5)
arrowhead([3.75, -1.5], [3.75, 1.5], 5,1,-0.5)

#the cubic and the circle
plot(x,fx, -2, 2)
arc([3.75, 0], 1, [0,360])

#the horizontal & vertical lines
linewidth(0.5)
setdash("[1 2] 0")
line([-2.0, fx(a)], [2.0, fx(a)])
line([d, -1.5], [d, 1.5])
line([3.75+cos(pi/3), -1.5], [3.75+cos(pi/3), 1.5])
setdash("[] 0")
linewidth(1.0)


#The intersections with the lines
roundPoint([a, fx(a)],  0.03)
roundPoint([b, fx(b)],  0.03)
roundPoint([c, fx(c)],  0.03)
roundPoint([d, fx(d)],  0.03)
roundPoint([3.75+cos(pi/3),  sin(pi/3)], 0.03)
roundPoint([3.75+cos(pi/3), -sin(pi/3)], 0.03)

#annotations
#annotate([2.0, 0.0], [2, -2], "$x$")
#annotate([0.0, 1.5], [-2, 4], "$y$")
#annotate([-1.0, 0.0], [0.0, -12.0], "$-1$")
#annotate([1.0, 0.0], [0.0, -12.0], "$1$")
annotate([x(-1.3), fx(-1.3)], [0.0, -12.0], "$y=x^3-x$")
closeOutputFile()


