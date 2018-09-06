#!/usr/bin/python
# Time-stamp: <2012-07-09 08:40:26 angenent>

from  grapher  import *
from math import *

def x(t): return t
def fx(t): return (3*t*(1-t))/(1+t*t)

amin=-1-sqrt(2)
apls=-1+sqrt(2)

setViewBox(-14, -4.5, 7, 2)
openOutputFile("05rationalexample", 360)
setlinecap(1)
axes()

setdash("[3] 0")
line([Viewxmin(), -3], [Viewxmax(), -3])
setdash("[] 0")
#the graph
linewidth(2)
setrgbcolor('red')
plot(x, fx, Viewxmin()+0.1, amin)
plot(x, fx, apls,  Viewxmax()-0.1)
setrgbcolor('blue')
plot(x, fx, amin, apls)
setrgbcolor('black')
linewidth(0.5)
line([apls, fx(apls)], [1,1])
line([amin, 0.14],[amin, fx(amin)])
line([apls, -0.14],[apls, fx(apls)])
linewidth(1)
for k in range(-13, 7):
    line([k,0], [k, -0.07])
    if k!=0:
        annotate([k,0], [0, 2],
             makeboxl(r"{\tiny\sffamily\upshape %d}"%(k)))
for k in range(-4, 2):
    line([0,k], [-0.07, k])
    if k!=0:
        annotate([0,k], [4, 0],
             makeboxc(r"{\tiny\sffamily\upshape %d}"%(k)))
roundPoint([amin, fx(amin)], 0.1)
roundPoint([apls, fx(apls)], 0.1)
roundPoint([0,0], 0.1)
roundPoint([1,0], 0.1)
#annotations
annotate([amin, fx(amin)], [-18, -12],"abs.~min.") 
annotate([1,1],[2,2],"abs.~max.")
annotate([amin, 0], [-3,   2], "$A$")
annotate([apls, 0], [-3, -10], "$B$")

closeOutputFile()


