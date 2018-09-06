## Time-stamp: Jul 25 08:46 01arcsine.py
from grapher import *
from math import *

def segment(a,b):
    plot(lambda t:sin(t), lambda t:t, a, b)

setViewBox(-1.5,-2.6, 1.5, 2.6)
openOutputFile("01arcsine",80)

axes([5,5])
linewidth(2)
setrgbcolor('blue')
segment(-pi/2, pi/2)
setrgbcolor('black')
linewidth(0.3)
setdash("[1 1]0")
linewidth(0.5)
polygonA([(0,-pi/2), (-1,-pi/2), (-1, 0)])
polygonA([(0,pi/2), (1,pi/2), (1, 0)])
setdash("[] 0")
roundPoint([0,pi/2], 0.04)
roundPoint([1,pi/2], 0.04)
roundPoint([0,-pi/2], 0.04)
roundPoint([-1,-pi/2], 0.04)
roundPoint([1, 0], 0.04)
roundPoint([-1, 0], 0.04)
annotate([0, pi/2], [-4, 0], makeboxr("$\pi/2$"))
annotate([0,-pi/2], [4, 0], makeboxl("$-\pi/2$"))
annotate([1, 0], [0,-12], makeboxc("$1$"))
annotate([-1, 0], [0,4], makeboxc("$-1$"))
annotate([0.2, 1.9], [0,0], makeboxl("$y=\\arcsin x$"))
closeOutputFile()
