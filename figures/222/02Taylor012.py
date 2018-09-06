#!/usr/bin/python
# Graph of e^x and first three Taylor polynomials.
from math import *
from grapher import *

def id(t): return t
def f(t): return exp(t)
def T0(t): return 1
def T1(t): return 1+t
def T2(t): return 1+t*(1+t*0.5)

def graph(filename, Tfunction, anno, Xanno, offs):
    setViewBox(-2, -0.25, 2, 3.0)
    openOutputFile(filename, 110)
    axes([5,5])
    setrgbcolor('red')
    plot(id, Tfunction,  Viewxmin(), Viewxmax())
    setrgbcolor('black')
    linewidth(0.5)
    plot(id, f, Viewxmin(), Viewxmax())
    linewidth(1)
    roundPoint([0,1], 0.03)
    annotate([log(3.0), 3.0], [0,2], makeboxc("\small$y=f(x)$"))
    annotate([Xanno, Tfunction(Xanno)], offs, makeboxl(anno))
    closeOutputFile()


graph("02Taylor012-0", T0, makeboxl("\small$y=T_0f(x)$"), -1.7, [0, 5])
graph("02Taylor012-1", T1, makeboxl("\small$y=T_1f(x)$"),  1.5, [0, -7])
graph("02Taylor012-2", T2, makeboxc("\small$y=T_2f(x)$"), -2.0, [0, 5])

