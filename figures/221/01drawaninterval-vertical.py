#!/usr/bin/python
# Time-stamp: Fri May 23 11:18:23 CDT 2008 angenent
from grapher import *
from math import *
import os

setViewBox(-0.5, -3.2, 0.5, 3.2)
openOutputFile("01drawaninterval-vertical",32)

linewidth(0.5)
line([0.0, -3.2],[0.0, 3.2])

for n in range(-3, 4, 1):
    line([0.05, n], [-0.05,n])
    annotate([0,n],[3,0],"$%d$"%(n))
A=[0,-1]
B=[0, 2]
linewidth(2)
line(A,B)
linewidth(1)
roundPoint(A,radius=0.04, fillcolor='black')
roundPoint(B,radius=0.04, fillcolor='white')

closeOutputFile()

