#!/usr/bin/python
## Time-stamp: Tue Oct 16 11:41:21 CDT 2007 angenent

from  grapher  import *
from math import *

def x(t): return t
def fx(t): return 0.6 - 0.5*sin(4*t)

def chord(a,b, color):
    AA=[a, fx(a)]
    BB=[b, fx(b)]
    setrgbcolor(color)
    line(AA, BB)
    setrgbcolor('black')
    roundPoint(AA, radius=0.02)
    roundPoint(BB, radius=0.02)

setViewBox(-0.1,-0.1, 1.5,1.6)
openOutputFile("05notconvex-margin", 90)

axes([5,5])
plot(x, fx,  Viewxmin(), Viewxmax())
linewidth(0.5)

chord(-0.05, 1.0,'blue')
chord(0.05, 0.7,'blue')
chord(0.2, 0.5,'blue')
chord(0.7, 1.47,'red')
chord(0.8, 1.3,'red')
chord(0.9, 1.2,'red')
chord(-0.02, 1.42,[0,196,0])
chord(0.03, 1.46, [0,196,0])

annotate([0.3, 1.4], [0,0], "{\\sffamily\\itshape not convex}")

closeOutputFile()


