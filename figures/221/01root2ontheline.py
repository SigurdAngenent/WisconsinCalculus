#!/usr/bin/python
# Time-stamp: Wed May 28 14:19:53 CDT 2008 angenent
from grapher import *
from math import *
import os

setViewBox(-2.2, -0.5, 2.2, 1.1)
openOutputFile("01root2ontheline",180)

roottwo=sqrt(2)
linewidth(0.5)
polygonA([[0,0], [0,1], [1,1], [1,0]])
line([-2.2, 0.0],[2.2, 0.0])
line([0,0], [1,1])
arc([0,0], roottwo, [0, 45])
arrowhead([roottwo-0.07, 1.0], [roottwo, 0.0], len=8, wid=2,overshoot=-1)

for n in range(-2, 3, 1):
	line([n,0.05], [n, -0.05])
	annotate([n,0],[-2,-10],"$%d$"%(n))

roundPoint([1.4142135,0], 0.02, r"$\sqrt2$")
closeOutputFile()

