#! /usr/bin/python
# Time-stamp: Wed Jun  4 12:47:50 CDT 2008 angenent

from grapher import *

def x(t): return t
def y(t): return 1.0/t
setViewBox(-2.0,-7.0, 5.0,7.0)
openOutputFile("03inverse-of-x",90)

#axes
axes([4,4])
#dotted line at the jump
setrgbcolor('blue')
plot(x, y, -1.95, -0.172)
arrow([x(-0.172), y(-0.172)], [x(-0.17), y(-0.17)], 8, 2)
setrgbcolor('red')
plot(x, y, 0.172, 4.9)
arrow([x(0.172), y(0.172)], [x(0.17), y(0.17)], 8, 2)
annotate([1,1], [2,2], makeboxl("$y=1/x$"))
annotate([0.2, 6.2], [0,0], makeboxl(r"$+\infty$?"))
annotate([-0.2, -6.2], [0,-5], makeboxr(r"$-\infty$?"))
closeOutputFile()


