#!/usr/bin/python
# Time-stamp : Fri Nov 30 16:18:35 CST 2007 angenent

from  grapher  import *
from math import *
################################################################################
Pmat=[]
def unitize(x):
    l=sqrt( sum([t*t for t in x]) )
    return [t/l for t in x]
def make_Pmat(viewp):
    """Orthogonal projection along the vector viewp"""
    global Pmat
    a = unitize( [-viewp[1], viewp[0], 0] )
    b = unitize( [-viewp[2]*viewp[0],
                  -viewp[2]*viewp[1], 
                  viewp[0]**2 + viewp[1]**2] )
    Pmat = zip(a,b)
def proj(X):  #linear projection of R^3 onto R^2 
  global Pmat
  x=sum([Pmat[i][0]*X[i] for i in range(3)])
  y=sum([Pmat[i][1]*X[i] for i in range(3)])
  return [x, y]
################################################################################
def jac(X, u, v):
  eps = 0.000001
  A = map(lambda p,q: (p-q)/eps, X(u+eps/2, v), X(u-eps/2, v))
  B = map(lambda p,q: (p-q)/eps, X(u, v+eps/2), X(u, v-eps/2))
  return A[0]*B[1]-A[1]*B[0]
def bisect(f, a, b):
  eps=0.000001
  fa, fb = f(a), f(b)
  if(fa*fb >0):
    print "\n==========NO ZERO FOUND IN BISECT.==========\n"
    return 0
  while(b-a > eps):
    c=(a+b)*0.5
    fc=f(c)
    if(fa*fc<=0):
      b, fb=c, fc
    else:
      a, fa=c, fc
  return c
def fold(t, zmin, zmax):
  return bisect(lambda z:jac(psurf, t, z), zmin, zmax)
def rad(x): return sqrt(1-x*x)
def surf(t, z):
  r=rad(t)
  return [t, r*cos(z), r*sin(z)]
def psurf(t,z): return proj(surf(t,z))
def surfin(t, z):
  r=0.5*rad(t)
  return [t, r*cos(z), r*sin(z)]
def psurfin(t,z): return proj(surfin(t,z))
def drawdiscF(t, fillcolor='lightGray'):
  ppout = [psurf(t, 2*i*pi/100) for i in range(101)]
  #ppin = [psurfin(t, 2*i*pi/100) for i in range(101)]
  #ppin.reverse()
  polygonF(ppout, fillcolor)
  #polygonF(ppin, fillcolor)
  polygonC(ppout)
  #polygonC(ppin)
################################################################################
# decide on a projection
make_Pmat([2,-5,1])

setViewBox(-2.0, -1.5, 2.0, 1.5)
openOutputFile("09sliced-sphere",120)

print "**********drawing the discs"
#x-axis and discs
line(proj([-1,0,0]), proj([0,0,0]))
drawdiscF(0)
line(proj([0,0,0]), proj([0.6,0,0]))
drawdiscF(1, 'black')
drawdiscF(0.65)
line(proj([0.65,0,0]), proj([0,0.8,0,0]))
drawdiscF(0.8)
line(proj([0.8,0,0]), proj([0.95,0,0]))
drawdiscF(0.95)
line(proj([0.95,0,0]), proj([1.3,0,0]))

print "**********drawing the graph of f"
#the graph of f
tt= [i/50.0 for i in range(-50, 51)]
linewidth(2)
polygonA([psurf(t, pi/2) for t in tt])
linewidth(1)


print "**********drawing arrows and annotations"
#Arrows

closeOutputFile()


