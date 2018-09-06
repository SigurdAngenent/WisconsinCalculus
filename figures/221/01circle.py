#!/usr/bin/python
## Time-stamp: <Wednesday February 18 2009 10:29:12>

from grapher import *
from math import *


beta=pi/4

setViewBox(-1.5,-1.5, 8.5,1.5)
openOutputFile("01circle",360)

#axes
linewidth(0.5)
for xo in (0, 3.5, 7.0):
    line([xo-1.5, 0], [xo+1.5, 0])
    arrowhead([xo-1.5, 0], [xo+1.5, 0], 5, 1.5, -0.5)
    line([xo, -1.2], [xo, 1.3])
    arrowhead([xo, -1.2], [xo, 1.3], 5, 1.5, -0.5)
linewidth(1.0)


#the circles
arc([0,0], 1, [0, 360])
arc([3.5, 0], 1, [0, 180])
arc([7.0, 0], 1, [180, 360])

#the vertical line
linewidth(0.5)
setdash("[1 2] 0")
line([cos(beta), -1], [cos(beta), 1])
setdash("[] 0")
linewidth(1)
roundPoint([cos(beta),  sin(beta)], 0.03)
roundPoint([cos(beta), -sin(beta)], 0.03)

#annotations
annotate([-0.4, 1.0], [0,  0], r"\makebox[0pt][r]{$x^2+y^2=1$}")
annotate([3.5+cos(beta),  sin(beta)], [3,  4], "$y=+\\sqrt{1-x^2}$")
annotate([7.0+cos(beta), -sin(beta)], [3, -6], "$y=-\\sqrt{1-x^2}$")
closeOutputFile()


