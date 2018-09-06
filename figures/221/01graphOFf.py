#!/usr/bin/python
## Time-stamp: Wed May 28 16:55:33 CDT 2008 angenent

import grapher
from math import *

def x(t):
    return t
def fx(t):
    t=(2-t)*(2-t)
    return 3/(1.0+t)

a=1.1
A=[a, 0]
B=[a, fx(a)]
C=[0, fx(a)]


grapher.setViewBox(-3.0, -0.1, 3.0, 3.5)
grapher.openOutputFile("01graphOFf",240)

#mark the domain
grapher.setrgbcolor('cyan')
grapher.polygonF([[-2,0],[2,0],[2,-0.06],[-2,-0.06],[-2,0]], 'cyan')
grapher.setrgbcolor('black')
grapher.axes()
#mark the range
grapher.setrgbcolor('magenta')
grapher.polygonF([[0,fx(-2.0)],
        [0.04, fx(-2)],
        [0.04,fx(2)],
        [0.0, fx(2)],
        [0.0, fx(-2)]], 'magenta')
grapher.setrgbcolor('black')
grapher.axes()

#the graph
grapher.plot(x,fx, -2, 2)

#the horizontal & vertical lines
grapher.setdash("[2] 0")
grapher.linewidth(0.5)
grapher.polygonA([A,B,C])
for t in (-2.0, 2.0):
    grapher.polygonA([[ t,0], [ t, fx( t)], [0,fx(t)]])

#draw arrowheads
grapher.setdash("[] 0")
for t in (-2.0, 2.0):
    grapher.arrowhead([ t, fx( t)], [0,fx(t)], 6,2,-1)
grapher.arrowhead(A, B, 7, 2, overshoot=-25)
grapher.arrowhead(A, B, 7, 2, overshoot=-55)
grapher.arrowhead(B, C, 7, 2, overshoot=-1)


grapher.roundPoint(A)
grapher.roundPoint(B)
grapher.roundPoint(C)

#annotations
grapher.annotate([-1,3], [0, 0], r"\makebox[0pt][r]{range of $f$}")
grapher.line([-1, 3], [00.025, 2.5])
grapher.annotate(C, [-2.0, 0.0], r"\makebox[0pt][r]{$y=f(x)$}")
grapher.annotate(B, [4.0, -2.0], "$(x, f(x))$")
grapher.annotate(A, [4.0, 2.0], "$x$")
grapher.annotate([0,0], [0, -12], r"\makebox[0pt][c]{domain of $f$}")
grapher.closeOutputFile()


