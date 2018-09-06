#!/usr/bin/python
# Time-stamp : Wed Dec  5 14:55:17 CST 2007 angenent
#
from grapher import *
from math import *

eps = 0.00001
def x(t): return t*t
def y(t): return 2*( -t+t*t*t/3.0 )
def Tx(t):
  global eps
  return (x(t+eps/2)-x(t-eps/2))/eps
def Ty(t):
  global eps
  return (y(t+eps/2)-y(t-eps/2))/eps

#setViewBox, openOutputFile
setViewBox(-1, -1.5, 5, 3)
openOutputFile("09arclength-Leibniz",170)
#draw curve
linewidth(0.3)
plot(x, y, -2, 2.8)
linewidth(1)
# draw dx-dy-ds triangle
tA, tB  = -1.5, -1.4
A=[ x(tA), y(tA) ]
B=[ x(tB), y(tB) ]
polygonF([A, [A[0], B[1]], B], "lightGray")
polygonC([A, [A[0], B[1]], B])
# annotations
annotate([ B[0], B[1] ],  [-4, -9], "$ds$")
annotate([ (A[0]+B[0])/2, B[1] ],  [0, 3], makeboxc("$dx$") )
annotate([ A[0], (A[1]+B[1])/2 ],  [3, -2], makeboxl("$dy$") )
 
closeOutputFile()



