#!/usr/bin/python
## Time-stamp: Wed May 28 10:08:07 CDT 2008 angenent

from  grapher  import *
from math import *

def x(t):    return t
def fx(t):    return 0.2+(t-0.3)**2

def chord(a,b, color):
    AA=[a, fx(a)]
    BB=[b, fx(b)]
    setrgbcolor(color)
    line(AA, BB)
    setrgbcolor('black')
    roundPoint(AA, radius=0.02)
    roundPoint(BB, radius=0.02)

setViewBox(-0.1,-0.1, 1.5,1.6)
openOutputFile("05convex", 120)

axes([5,5])
linewidth(1)
plot(x, fx,  Viewxmin(), Viewxmax())
linewidth(0.5)

chord(-0.05, 1.4,'blue')
chord(0.0, 1.1, 'blue')
chord(0.05, 0.9, 'blue')
chord(0.1, 0.5,'blue')
chord(0.6, 1.2,[0, 128, 0])
chord(0.3, 1.3,'ocean')

annotate([0.3, 1.4], [0,0], "convex")

closeOutputFile()


