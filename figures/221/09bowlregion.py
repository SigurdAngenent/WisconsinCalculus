#!/usr/bin/python
# Time-stamp : Thu Nov 29 13:21:40 CST 2007 angenent
#
from  grapher  import *
from math import *



setViewBox(-0.5,-0.2,2.5,1.6)
openOutputFile("09bowlregion",90)

axes([5,5])
exxes = [-1+0.02*k for k in range(101)]
curve = [[1+x, x*x] for x in exxes]
curve.append(curve[0])
setrgbcolor('lightGray')
polygonF(curve)
setrgbcolor('black')
polygonA(curve)

setdash("[3] 0")
linewidth(0.5)
line([2,0], [2,1])

annotate([0, 1], [-7, -2], "1")
annotate([1, 0], [-2, -10], "1")
annotate([2, 0], [-2, -10], "2")
annotate([1, 0.5], [-1, -2], "$\setR$")

closeOutputFile()


