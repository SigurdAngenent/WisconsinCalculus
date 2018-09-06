#!/usr/bin/python
## Time-stamp: 

from  grapher  import *
from math import *

def x(t): return t

setViewBox(-3.1, -0.1, 3.1, 3.1)
openOutputFile("07expplot",270)

#draw the multicolor graph paper
linewidth(0.1)
setrgbcolor([128, 255, 255])
grid(-3, 3, 0.1, 0, 3, 0.1)
setrgbcolor([0,128, 255])
grid(-3, 3, 1.0, 0, 3, 1.0)
setrgbcolor('black')
linewidth(1)
axes([5,5])

#draw the graphs
plot(x, lambda x: 2.0**x, Viewxmin() + 0.25, Viewxmax() - 0.25)
plot(x, lambda x: 3.0**x, Viewxmin() + 0.25, Viewxmax() - 0.25)
plot(x, lambda x: 0.5**x, Viewxmin() + 0.25, Viewxmax() - 0.25)
plot(x, lambda x: 3.0**(-x), Viewxmin() + 0.25, Viewxmax() - 0.25)
plot(x, lambda x: 0.8**x, Viewxmin() + 0.25, Viewxmax() - 0.25)

for k in range(-3, 4):
    annotate([k,0], [-2, -12], "%2d"%(k))

for k in range(2, 4):
    annotate([0,k], [3, -3], "%1d"%(k))

closeOutputFile()


