#! /usr/bin/python

from grapher import *
from math import *

def x(t):  return (t)
def fx(t): return t*cos(pi/t)

setViewBox(-1.7,-1.4,1.7,1.4)
openOutputFile("03backwardCosSandwich",270)

axes([5,5])

linewidth(0.5)
setrgbcolor('ocean')

tmax=1.5
for k in range(5):
    plot(x,fx, tmax/4, tmax)
    plot(x,fx, -tmax/4, -tmax)
    tmax/=4
linewidth(0.1)
setrgbcolor('blue')
h=0.02
polygonF([[-1.3,-1.3], [0,0], [1.3, -1.3],
          [1.3,-1.3-h], [0,0-h], [-1.3, -1.3-h]],
         fillcolor='green')
polygonC([[-1.3,-1.3], [0,0], [1.3, -1.3],
          [1.3,-1.3-h], [0,0-h], [-1.3, -1.3-h]])
# setdash("[2 4] 0")
# polygonA([[-1.3,-1.3], [0,0], [1.3, -1.3]])
# setdash("[] 0")
linewidth(0.1)
setrgbcolor('red')
h=0.02
polygonF([[-1.3,1.3], [0,0], [1.3, 1.3],
          [1.3,1.3+h], [0,0+h], [-1.3, 1.3+h]],
         fillcolor='yellow')
polygonC([[-1.3,1.3], [0,0], [1.3, 1.3],
          [1.3,1.3+h], [0,0+h], [-1.3, 1.3+h]])
setdash("[1 2] 0")
linewidth(0.5)
setrgbcolor('black')
line([1,0.02], [1, fx(1)])
setdash("[] 0")
line([-1,-0.02], [-1, 0.02])
for ex in [1.0, 0.5, -2.0/3]:
    roundPoint([ex, fx(ex)], 0.02)
annotate([1.0, fx(1.0)], [2,2], makeboxl("$A$") )
annotate([0.5, fx(0.5)], [-1,1], makeboxr("$B$") )
annotate([-2.0/3, fx(-2.0/3)], [2,2], makeboxl("$C$") )
annotate([1,0], [0,5], makeboxc("$1$") )
annotate([-1,0], [0,5], makeboxc("$-1$") )
annotate([-0.7, 0.7], [1,3], makeboxl("$y=|x|$") )
annotate([-0.7,-0.7], [1,-9], makeboxl("$y=-|x|$") )

closeOutputFile()


