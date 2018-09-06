#!/usr/bin/python
## Time-stamp: <2012-07-13 15:19:50 angenent>
from grapher import *
from math import *

def f(t): return (x-0.4)**2 + 0.25
a=1.0
dx=0.3
n=20
tt1 = [0.51+k*(a-0.5)/n for k in range(n+1)]
tt2 = [a+k*(dx/n) for k in range(n+1)]
tt3 = [a+dx+k*(2-a-dx)/n for k in range(n+1)]

gr1 = [(x, f(x)) for x in tt1]
gr2 = [(x, f(x)) for x in tt2]
gr3 = [(x, f(x)) for x in tt3]

def drawfigure(title, albl, xlbl, falbl, fxlbl):
    global gr1, gr2, gr3
    setViewBox(0.5,-0.05, 2, 2)
    openOutputFile(title,72)
    axes([5,5])
    linewidth(2)
    polygonA(gr2)
    polygonA([gr2[-1], [gr2[-1][0], gr2[0][1]], gr2[0]])
    setrgbcolor('black')
    linewidth(0.3)
    for j in (-1,0):
        polygonA([ [gr2[j][0], 0] ,
                   gr2[j],
                   [0, gr2[j][1]] ] )
    polygonA(gr1)
    polygonA(gr3)

    annotate([gr2[0][0], 0], [0, -8], makeboxc(albl))
    annotate([gr2[-1][0], 0], [-2, -8], makeboxl(xlbl))
    annotate([gr2[-1][0], gr2[0][1]], [2,-2],  makeboxl(falbl))
    annotate(gr2[-1], [2,-2],  makeboxl(fxlbl))

    closeOutputFile()

drawfigure("04derivative-notation-ax", r"$a$", r"$x$", r"$f(a)$", r"$f(x)$")
drawfigure("04derivative-notation-xDx",
           r"$x$", r"$x+\Delta x$", r"$f(x)$", r"$f(x+\Delta x)$")
drawfigure("04derivative-notation-xh",
           r"$x$", r"$x+h$", r"$f(x)$", r"$f(x+h)$")
drawfigure("04derivative-notation-ah",
           r"$a$", r"$a+h$", r"$f(a)$", r"$f(a+h)$")



