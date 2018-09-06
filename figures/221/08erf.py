#!/usr/bin/python

from grapher import *
from math import *

def id(t): return t
def f(x): return (2/sqrt(pi))*exp(-x*x)


setViewBox(-3,-0.2,3,2)
openOutputFile("08erf",270)



a=1.25
N=100
dx=a/N
region = [ [i*dx, f(i*dx)] for i in range(N+1)]
region.append([a,0])
region.append([0,0])
region.append([0,f(0)])
setrgbcolor('gray')
polygonF(region)
setrgbcolor('black')
polygonC(region)

axes()
plot( id, f,  Viewxmin(), Viewxmax() )

linewidth(0.5)
line([0.5, 0.5*f(0.5)], [1, 1])
annotate([1,1], [1,1], "Area $=\\erf(x)$")
line([-0.5, f(0.5)], [-1, 1.3])
annotate([-1, 1.3], [-18, 7], "$y=\\frac2{\\sqrt\\pi}e^{-x^2}$")
annotate([a,0], [0,-12], "$x$")
closeOutputFile()


