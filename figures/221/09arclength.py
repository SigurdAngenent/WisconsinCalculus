#!/usr/bin/python
# Time-stamp: Aug  7 15:19 09arclength.py
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
openOutputFile("09arclength",170)
# compute partition, polygon
pttn=[-2.0+i*0.6 for i in range(8)]
vertices =[[x(t), y(t)] for t in pttn] 
setrgbcolor('red')
linewidth(0.6)
polygonA(vertices)
setrgbcolor('black')
# draw dx-dy-ds triangle
A=vertices[5]
B=vertices[6]
linewidth(1.5)
polygonF([A, [B[0], A[1]], B], "lightGray")
polygonA([A, [B[0], A[1]], B])
setrgbcolor('red')
line(A, B)
setrgbcolor('black')
linewidth(1)
plot(x, y,  pttn[0], pttn[-1])
# draw polygon
k=0
for t in pttn:
    P=[x(t), y(t)]
    vx, vy  = Tx(t), Ty(t)
    v=sqrt(vx*vx+vy*vy)
    nx, ny = vy/v, -vx/v
    roundPoint(P, 0.05)
    if k<3:
        annotate([P[0]+0.3*nx , P[1]+0.3*ny], [0,0], 
                makeboxc("$P_%1d$"%(k)) )
    k+=1
# annotations
linewidth(0.2)
line( [A[0]-0.3, A[1]-0.3], [A[0]-0.05, A[1]-0.05] )
annotate([A[0]-0.3, A[1]-0.3], [0, -6], makeboxc("$P_{k-1}$") )
annotate(B, [-4, 4], makeboxc("$P_{k}$") )
annotate(vertices[-1], [2, 4], makeboxc("$P_{n}$") )
annotate([ (A[0]+B[0])/2, A[1] ],  [-5, -10], "$\\Delta x_k$")
annotate([ B[0], (A[1]+B[1])/2 ],  [3, -2], "$\\Delta y_k$")
annotate([ (A[0]+B[0])/2, (A[1]+B[1])/2 ],  [-2, 2],
        makeboxr("$\\Delta s_k$") )
 
closeOutputFile()


