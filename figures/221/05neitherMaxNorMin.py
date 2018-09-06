#!/usr/bin/python
## Time-stamp: Wed May 28 09:51:37 CDT 2008 angenent

from  grapher  import *
from math import *

def x(t): return t
def fx(t): return t*t*t


setViewBox(-1,-1, 1,1)
openOutputFile("05neitherMaxNorMin",90)

axes([5,5])
linewidth(1)
plot(x, fx,  Viewxmin(), Viewxmax())
#linewidth(1)

setrgbcolor('red')
line([-0.5, 0], [0.5, 0])
roundPoint([0,0], radius=0.03)

annotate([0.2, 0.8], [0,0], "$y=x^3$")


closeOutputFile()


