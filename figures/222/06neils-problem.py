#!/usr/bin/python
# Solution to the right angle problem
from math import *
from grapher import *

def x(t): return t*t

def y(t): return t*t*t


setViewBox(-0.2,-1.1, 1, 1.1)
openOutputFile("06neils-problem", 72)

axes([5,5])
plot(x, y,-1,1)
annotate([x(0.8),  y(0.8)], [1,-8], makeboxl(r"$y = x^{3/2}$"))
annotate([x(0.8), -y(0.8)], [1, 2], makeboxl(r"$y =-x^{3/2}$"))
closeOutputFile()


