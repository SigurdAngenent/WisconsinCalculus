#!/usr/bin/python
## Time-stamp: <Thursday May 03 2012 19:23:26>

from grapher import *
from math import *

def segment(a,b):
    plot(lambda t:t, lambda t:tan(t), a, b)

Height = 4.0
setViewBox(-1.6*pi,-Height, 1.6*pi,Height)
openOutputFile("01tangent",180)

axes([5,5])
linewidth(2)
setrgbcolor('red')
segment(-pi/2+0.1, pi/2-0.1)
setrgbcolor('black')
linewidth(0.3)
setdash("[1 1]0")
segment(-3*pi/2+0.1, -pi/2-0.1)
segment( 3*pi/2-0.1,  pi/2+0.1)
linewidth(0.5)
for x in (-1.5*pi, -pi/2, +pi/2, 1.5*pi):
    line((x, -Height+0.2), (x, Height-0.2))
setdash("[] 0")

linewidth(3)
setrgbcolor("white")
for k in (-3, -1, 1, 3):
    line((k*pi/2, 0.1), (k*pi/2, 0.7))
linewidth(1)
annotate([-3*pi/2, 0], [-4, 5], makeboxc("$-\\frac{3\pi}2$"))
annotate([-1*pi/2, 0], [-2, 5], makeboxc("$-\\frac{\pi}2$"))
annotate([1*pi/2, 0], [0, 5], makeboxc("$\\frac{\pi}2$"))
annotate([3*pi/2, 0], [0, 5], makeboxc("$\\frac{3\pi}2$"))
annotate([pi/2, Height], [0,5], makeboxc("$y = \\tan x$"))

closeOutputFile()




