#!/usr/bin/python
## Time-stamp: 

from  grapher  import *
from math import *

def x(t): return t

setViewBox(-0.1, -3, 10, 3)
openOutputFile("07logplot",360)

#draw the multicolor graph paper
linewidth(0.1)
setrgbcolor([128, 255, 255])
grid(0, 10, 0.1, -3, 3, 0.1)
setrgbcolor([0,128, 255])
grid(0, 10, 1.0, -3, 3, 1.0)
setrgbcolor('black')
linewidth(1)
axes([5,5])


plot(x, lambda x: log(x)/log(2), 0.02, Viewxmax())
plot(x, lambda x: log(x)/log(3), 0.02, Viewxmax())
plot(x, lambda x: -log(x)/log(2), 0.02, Viewxmax())
plot(x, lambda x: -log(x)/log(3), 0.02, Viewxmax())
setrgbcolor('red')
plot(x, lambda x: log(x)/log(10), 0.02, Viewxmax())

for k in range(1, 11):
    annotate([k,0], [-2, -12], "%2d"%(k))

for k in range(-3, 4):
    annotate([0,k], [-10, -3], "%1d"%(k))

closeOutputFile()


