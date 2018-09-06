#!/usr/bin/python
# Time-stamp: <2012-07-30 11:42:03 angenent>

from grapher import *
from math import *

def id(t): return t
def f(x): return (2-x) * x * 0.5
def g(x): return exp(x/3)+(1-x/1.7)**2-0.6


setViewBox(-0.1, -0.2, 2.5, 1.6)
openOutputFile("09areabetweengraphs-setup",150)

n=200

a=0.2
b=1.7
dx = (b-a)/n

linewidth(1.5)
region = [ (a+i*dx, g(a+i*dx)) for i in range(n+1)]
region.extend([ (a+i*dx, f(a+i*dx)) for i in range(n, -1, -1) ])
polygonF(region, 'gray')
polygonC(region)

linewidth(0.4)
plot(id, f,  Viewxmin(), Viewxmax())
plot(id, g,  Viewxmin(), Viewxmax())

linewidth(0.5)
setdash("[3] 0")
line([a,0], [a, f(a)])
line([b,0], [b, f(b)])
setdash("[] 0")

x_axis(5)

roundPoint([a,0], 0.015)
roundPoint([b,0], 0.015)

annotate([a,0], [-2,-12], "$a$")
annotate([b,0], [-2,-12], "$b$")

bb=(2*a+b)/3
annotate([bb, g(bb)], [0, 4], "$y=g(x)$")
annotate([bb,f(bb)], [0, -10], "$y=f(x)$")
closeOutputFile()


