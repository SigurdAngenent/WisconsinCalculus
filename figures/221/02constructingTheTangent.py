#!/usr/bin/python

import grapher

def x(t): return t
def fx(t): return t*t
def fxp(t): return 2*t
def tangent(t, a): return fx(a)+(t-a)*fxp(a)
def secant(t, a, b): return fx(a)+(t-a)*(fx(b)-fx(a))/(b-a)
def drawsecant(xmin, xmax,a,b):
    grapher.line([xmin, secant(xmin, a, b)], [xmax, secant(xmax, a, b)])

a=0.4
b=1.2
c=(a+b)/2
d=(b+c)/2
#Draw the graph of f, the tangent at x=a and the secant from x=a to x=b
#   and some more dashed secants from a to c, c', c", etc.

grapher.ViewBox=[-0.5,-0.5,2.0,2.0]
grapher.openOutputFile("02constructingTheTangent",270)

#the graph and the tangent
grapher.axes()
grapher.plot(x,fx,-0.5, 1.5)
grapher.line([-0.5,tangent(-0.5, a)],[1.5,tangent(1.5, a)])

#the arrow indicating motion of Q
grapher.linewidth(3)
grapher.plot(x, fx, d, b)
grapher.linewidth(1)
grapher.arrowhead([b, tangent(b,d)], [d, fx(d)],  len=10, wid=5, overshoot=4)

# The secants
grapher.linewidth(0.5)
grapher.line([0.0,secant(0.0, a, b)],[1.5, secant(1.5, a, b)])
grapher.setdash("[1 2] 0")
clist = ((a+2*b)/3, (2*a+b)/3,  (5*a+b)/6, (9*a+b)/10,
         (15*a+b)/16, (31*a+b)/32, (63*a+b)/64)
for z in clist:
    drawsecant(-0.1, 1.5, a, z)
grapher.setdash("[] 0")

#Points and annotations
grapher.linewidth(1.0)
grapher.setrgbcolor('red')
rad=0.02
for z in clist:
    grapher.roundPoint([z, fx(z)], rad)
    rad*=0.75
grapher.roundPoint([a, fx(a)], 0.02)
grapher.roundPoint([b, fx(b)], 0.02)

grapher.annotate([a, fx(a)], [-2,0], r"\makebox[0pt][r]{$P$}")
grapher.annotate([b, fx(b)], [-2,0], r"\makebox[0pt][r]{$Q$}")
grapher.annotate([1.5, tangent(1.5, a)], [2,0], "tangent")
grapher.annotate([1.5,  secant(1.5, a, b)], [2,0], "a secant")
#grapher.annotate([1.5,  secant(1.5, a, c)], [2,0], "another secant")

grapher.closeOutputFile()


