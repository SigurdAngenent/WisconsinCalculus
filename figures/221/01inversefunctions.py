#!/usr/bin/python
# Time-stamp : Thu May 29 16:11:48 CDT 2008 angenent
#
from grapher import *
from math import *

def f(t):
    return 0.75*t*t*t
def hook(a):
    return [[a, 0.0], [a, f(a)], [0, f(a)]]
def kooh(a):
    global b
    return [[b,a], [b+f(a), a], [b+f(a), 0]]

b=3.0

setViewBox(-0.2, -0.2, 2*b+0.2, 2.6)
openOutputFile("01inversefunctions",300)

#The graphs
plot( lambda t:t, f, 0, 1.5)
plot( lambda t:b+f(t), lambda t : t, 0, 1.5)

#Axes
linewidth(0.5)
line([0,0], [b-0.5,0])
line([0,0], [0, 2.5])
line([b, 0], [b+2.5, 0])
line([b, 0], [b, 2.5])
arrowhead([0,0], [b-0.5,0], 7, 2)
arrowhead([b,0], [b+2.5, 0], 7, 2)
arrowhead([0,0], [0, 2.5], 7, 2)
arrowhead([b,0], [b, 2.5], 7, 2)

setdash("[1 2] 0")
for z in ( ('a',0.5), ('b',1.0), ('c',1.4)):
    polygonA(hook(z[1]))
    annotate([z[1], 0], [0,-10], r"\makebox[0pt][c]{$"+z[0]+"$}")
    annotate([0, f(z[1])], [-2,0], r"\makebox[0pt][r]{$f("+z[0]+")$}")
    polygonA(kooh(z[1]))
    annotate([b+f(z[1]), 0], [0,-10], r"\makebox[0pt][c]{$f("+z[0]+")$}")
    annotate([b+0, z[1]], [-2,0], r"\makebox[0pt][r]{$"+z[0]+"$}")

setdash("[] 0")
annotate([0.1, 2.6], [0,0], r"The graph of $f$")
annotate([0.3+b, 1.8], [0,0], r"The graph of $f^{-1}$")

closeOutputFile()


