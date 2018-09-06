#!/usr/bin/python
# Graph of e^x and first three Taylor polynomials.
from math import *
from grapher import *

def id(t): return t
def f(t): return exp(t)
def T0(t): return 1
def T1(t): return 1+t
def T2(t): return 1+t*(1+t*0.5)


setViewBox(-2, -0.25, 2, 2.0)
openOutputFile("02Taylor012-1", 120)
axes([5,5])


plot(id, T1,  Viewxmin(), Viewxmax())
linewidth(0.5)
plot(id, f, Viewxmin(), Viewxmax())

annotate([log(1.8), 1.8], [5,0], makeboxl("\small$y=e^{x}$"))
annotate([-1.7, 1], [0, 3], makeboxl("\small$y=T_0e^x$"))
closeOutputFile()


