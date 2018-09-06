#!/usr/bin/python
# Time-stamp :  
#
from  grapher  import *
from math import *

def x(t):
    return t
def fx(t):
    return t*t

a=1.0
b=1.5
A=[a, fx(a)]
B=[b, fx(b)]

setViewBox(-0.8,-0.2,2.0,2.7)
openOutputFile("02DeltaxDeltay",120)

y_axis(arrowsize=7)
line([-0.4, 0], [2.0, 0])
arrowhead([-0.4, 0], [2.0, 0], 7, 7*0.3, overshoot=-0.1)
plot(x, fx,  0, 1.6)
linewidth(0.5)
polygonA([A, [b, fx(a)], B])
setdash("[1 2] 0")
polygonA([[a, 0], A, [0, fx(a)]])
line([b, 0], [b, fx(a)])
line(B, [0, fx(b)])
setdash("[] 0")

roundPoint(A, 0.02)
roundPoint(B, 0.02)

annotate([(a+b)/2, fx(a)], [0, -10], r"\makebox[0pt][c]{$\Delta x$}")
annotate([b, (fx(a) + fx(b))/2], [2, 0], r"\makebox[0pt][l]{$\Delta y$}")
annotate(A, [0, 2], r"\makebox[0pt][r]{$P$}")
annotate(B, [0, 2], r"\makebox[0pt][r]{$Q$}")
annotate([a, 0], [0, -8], r"\makebox[0pt][c]{$1$}")
annotate([b, 0], [0, -8], r"\makebox[0pt][c]{$x$}")
annotate([0, fx(a)], [-4, 0], r"\makebox[0pt][r]{$1$}")
annotate([0, fx(b)], [-4, 0], r"\makebox[0pt][r]{$x^2$}")


closeOutputFile()


