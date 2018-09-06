#!/usr/bin/python
# Time-stamp: Thu May 29 11:29:32 CDT 2008 angenent
from  grapher  import *
from math import *

def ell(x):
    return 0.6*x+0.4
def L(x):
    return [x, ell(x)]

setViewBox(-0.5, -0.5, 3.0, 2.0)
openOutputFile("01line",240)
axes()

line([-0.5, ell(-0.5)], [2.8, ell(2.8)])
line([0.5, ell(0.5)], [1.5, ell(0.5)])
line([1.5, ell(0.5)], [1.5, ell(1.5)])
polygonA([L(2.1), [2.5, ell(2.1)], L(2.5)])

linewidth(0.5)
setdash("[2] 0")
polygonA([[0,ell(0.5)], [0.5, ell(0.5)], [0.5, 0.0]])
line([0,ell(1.5)], [1.5, ell(1.5)])
line([1.5, 0.0], [1.5, ell(0.5)])
setdash("[] 0")

roundPoint([0.5, ell(0.5)],0.015)
annotate([0.5, ell(0.5)],[-4, 8],"$P_0$") 
roundPoint([1.5, ell(1.5)],0.015)
annotate([1.5, ell(1.5)],[-4, 8],"$P_1$") 
annotate([1.5, ell(1.0)],[4, 0], "$y_1-y_0$")
annotate([1.0, ell(0.5)],[0, -10], r"\makebox[0pt][c]{$x_1-x_0$}")
annotate([0.5, 0.0], [-4, -12], "$x_0$")
annotate([1.5, 0.0], [-4, -12], "$x_1$")
annotate([0.0, ell(0.5)], [-10, 0], "$y_0$")
annotate([0.0, ell(1.5)], [-10, 0], "$y_1$")
annotate([0.0, ell(0.0)], [-2,1], r"\makebox[0pt][r]{$n$}")
annotate([2.3, ell(2.1)], [0,-8], r"$1$")
annotate([2.5, ell(2.3)], [2,-1], r"$m$")
roundPoint([0.0, ell(0.0)])
closeOutputFile()


