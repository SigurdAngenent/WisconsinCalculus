#!/usr/bin/python
## Time-stamp: <2012-07-19 20:05:27 angenent>

from  grapher  import *
from math import *

setViewBox(-3.1, -8, 3.1, 8)
openOutputFile("05intermediatevalue-fail", 75)
axes([5,5])

for x in (-2.0, 2.0):
    line([x,-0.2/x], [x, 0.2/x])


#the graph
setrgbcolor('red')
plot((lambda t: t), (lambda t: 1/t), -2.0, -0.128)
plot((lambda t: t), (lambda t: 1/t),  0.128, 2.0)
roundPoint([-2,-0.5], 0.1)
roundPoint([ 2, 0.5], 0.1)

annotate([1.0/3, 3], [2,3], makeboxl(r"$y=1/x$") )
annotate([-2,0], [0,3], makeboxc(r"$-2$") )
annotate([ 2,0], [0,-8], makeboxc(r"$+2$") )
closeOutputFile()


