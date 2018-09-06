#!/usr/bin/python
# Graph of sin x and its first few Taylor polynomials.
from math import *
from grapher import *

def id(t):  return t
def f(t):   return sin(t)
def T1(t):  return t
def T3(t):  return t*(1-t*t/(2*3))
def T5(t):  return t*(1-t*t/(2*3)*(1-t*t/(4*5)))
def T7(t):  return t*(1-t*t/(2*3)*(1-t*t/(4*5)*(1-t*t/(6*7))))
def T9(t):  return t*(1-t*t/(2*3)*(1-t*t/(4*5)*(1-t*t/(6*7)*(1-t*t/(8*9)))))
def T11(t): return t*(1-t*t/(2*3)*(1-t*t/(4*5)*(1-t*t/(6*7)*(1-t*t/(8*9)*(1-t*t/(10*11)))))) 
#  Main
setViewBox(-8.0, -2.5, 8.0, 2.5)
openOutputFile("02sint", 360)

axes([7,7])

linewidth(1)
setrgbcolor([0,192,0])
plot(id, f, -8, 8)

linewidth(0.5)
setrgbcolor('blue')
plot(id, T1, -8, 8)
plot(id, T3, -8, 8)
setrgbcolor('red')
plot(id, T5, -8, 8)
plot(id, T7, -8, 8)
setrgbcolor('magenta')
plot(id, T9, -8, 8)
plot(id, T11, -8, 8)
# Annotations
annotate([  pi, 0], [2, 2], makeboxl(r"$\pi$"))
annotate([2*pi, 0], [2, 2], makeboxr(r"$2\pi$"))
annotate([ -pi, 0], [-2, -8], makeboxr(r"$-\pi$"))
annotate([-2*pi, 0], [-2, -8], makeboxl(r"$-2\pi$"))

annotate([8, f(8)], [3, -2], makeboxl(r"$y=\sin x$"))
annotate([2.5, 2.5], [0, 4], makeboxc(r"$T_1f(x)$"))
annotate([4.5, 2.5], [0, 4], makeboxc(r"$T_5f(x)$"))
annotate([5.5, 2.5], [0, 4], makeboxl(r"$T_9f(x)$"))

annotate([3.0, -2.5], [0, -9], makeboxc(r"$T_3f(x)$"))
annotate([4.8, -2.5], [0, -9], makeboxc(r"$T_7f(x)$"))
annotate([6.0, -2.5], [0, -9], makeboxl(r"$T_{11}f(x)$"))

closeOutputFile()


