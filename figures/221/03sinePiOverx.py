#!/usr/bin/python

from grapher import *
from math import *

def x(t): return 1.0/(t)
def fx(t): return sin(pi*t)

setViewBox(-3.2,-1.2, 3.2,1.2)
openOutputFile("03sinePiOverx",360)

axes([5,5])

#dashed lines
linewidth(0.5)
setdash("[2] 0")
line([-3,1], [3,1])
line([-3,-1], [3,-1])
line([2,0], [2,1])
setdash("[] 0")

#the sine curve
setrgbcolor('blue')
tmin=0.333333333
for n in range(4):
    plot(x,fx, tmin, 3.0*tmin)
    plot(x,fx, -tmin, -3.0*tmin)
    tmin=3*tmin

#mark interesting points
setrgbcolor('black')
for P in [[0.5,0], [1,0], [2,0], [2,1], [3,0],
        [2.0/3, -1], [0.4, 1], [-1,0], [2.0/7, -1], [-0.4, -1]]:
    roundPoint(P, 0.02)

annotate([x(1.2), fx(1.2)], [4.0, -12.0], r"$y=\sin\frac\pi x$")
for j in[1,2,3]:
    annotate([j,0], [0,-10], makeboxl(r"$%d$"%(j)) )
annotate([0.5,0], [1,5], makeboxl(r"$\tfrac12$") )
annotate([2.0/3,-1], [0,-10], makeboxc(r"$A$") )
annotate([  0.4, 1], [0,4], makeboxc(r"$B$") )
annotate([2.0/7,-1], [0,-10], makeboxc(r"$C$") )
annotate([   -1, 0], [0,-10], makeboxl(r"$D$") )
annotate([ -0.4,-1], [0,-10], makeboxc(r"$E$") )


closeOutputFile()


