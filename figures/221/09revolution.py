#!/usr/bin/python
# Time-stamp : Tue Nov 27 16:35:01 CST 2007 angenent

from  grapher  import *
from math import *



Pmat=[[0.8,-0.2], [0.3, 0.1], [0, 1]]

def proj(X):
  global Pmat
  x=sum([Pmat[i][0]*X[i] for i in range(3)])
  y=sum([Pmat[i][1]*X[i] for i in range(3)])
  return [x, y]

setViewBox(-0.5, -1.5, 4.0, 1.5)
openOutputFile("09revolution",270)

line(proj([0,0,0]), proj([4,0,0]))
circle = [[1, cos(k*pi/50), sin(k*pi/50)] for k in range(101)]
circle = [proj(P) for P in circle]
polygonA(circle)
line(proj([1, 0, 0]), proj([1, cos(0.3), sin(0.3)]))

closeOutputFile()


