#!/usr/bin/python
## Time-stamp: <Thursday May 03 2012 19:22:36>

from grapher import *
from math import *

def segment(a,b):
    plot(lambda t:tan(t), lambda t:t, a, b)

Height = 4.0
setViewBox(-Height, -2.0, Height, 2.0)
openOutputFile("01arctangent",180)

axes([5,5])
linewidth(2)
setrgbcolor('red')
segment(-pi/2+0.1, pi/2-0.1)
setdash("[1 1]0")
setrgbcolor('black')
linewidth(0.5)
for x in (-pi/2, +pi/2):
    line((-Height+0.2, x), (Height-0.2, x))
setdash("[] 0")
linewidth(2)
setrgbcolor("white")
line((0.1, pi/2), (0.8, pi/2))
line((0.1, -pi/2), (1.2, -pi/2))


annotate([0, -pi/2], [2, -2], makeboxl("$-\pi/2$"))
annotate([0, pi/2],  [2, -2], makeboxl("$\pi/2$"))
annotate([-Height+1.5, -0.8], [0,0], makeboxc("$y=\\arctan x$"))

closeOutputFile()




