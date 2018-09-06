#!/usr/bin/python
# Solution to the right angle problem
from math import *
from grapher import *

def x(t): return t/(1.0+t*t*t*t)

def y(t): return t*t


setViewBox(-1, -0.2, 1, 5)
openOutputFile("06sketchme-problem", 72)

axes([5,5])
plot(x, y, -2.2, 2.2)
closeOutputFile()


