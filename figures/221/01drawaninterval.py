#!/usr/bin/python
# Time-stamp: Fri May 23 11:18:23 CDT 2008 angenent
from grapher import *
from math import *
import os

setViewBox(-3.2, -0.5, 3.2, 0.5)
openOutputFile("01drawaninterval",240)

linewidth(0.5)
line([-3.2, 0.0],[3.2, 0.0])

for n in range(-3, 4, 1):
    line([n,0.05], [n, -0.05])
    annotate([n,0],[-2,-10],"$%d$"%(n))
A=[-1,0]
B=[2,0]
linewidth(2)
line(A,B)
linewidth(1)
roundPoint(A,radius=0.04, fillcolor='black')
roundPoint(B,radius=0.04, fillcolor='white')

closeOutputFile()

