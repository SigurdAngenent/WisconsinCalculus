#!/usr/bin/python
## Time-stamp: Tue Oct 16 11:41:21 CDT 2007 angenent
# Time-stamp: <2012-07-20 11:11:39 angenent>
from grapher import *
from math import *

def x(t): return t
def fx(t): return -t**5/15.0+0.8*t*t-t+0.8
def dfx(t): 
    eps=1e-8
    return ( fx(t+eps) - fx(t-eps) ) / (2*eps)
def tangentSegment(t, seglen=0.5):
    vx=1
    vy=dfx(t)
    v=sqrt(vx*vx+vy*vy)
    vx, vy= vx/v, vy/v
    xx, yy = x(t), fx(t)
    line([xx- seglen*vx, yy-seglen*vy],\
         [xx+ seglen*vx, yy+seglen*vy])
    roundPoint([xx, yy], 0.03)

setViewBox(-0.8,-0.5, 2.5,2.0)
openOutputFile("05mvt2",180)

a = -0.4
b = 1.8
m = (fx(b)-fx(a))/(b-a)
n=200 # number of sample points to find c
xx = [a + k*(b-a)/n for k in range(n+1)]
dd = [fx(t)-m*t for t in xx]
dmin = min(dd)
dmax = max(dd)
c = xx[ dd.index(dmin) ]
c2 = xx[ dd.index(dmax) ]
x_axis()
linewidth(0.2)
setdash('[1] 0')
plot(x, fx,  Viewxmin(), a)
plot(x, fx, b, Viewxmax())
linewidth(3)
plot(x, fx, a, b)
linewidth(1)

setdash('[2] 0')
setrgbcolor('blue')
line([a, 0], [a, fx(a)])
line([b, 0], [b, fx(b)])
setdash('[] 0')
roundPoint([a, 0],0.03)
roundPoint([b, 0],0.03)

line([a, fx(a)], [b, fx(b)])
roundPoint([a, fx(a)],0.03)
roundPoint([b, fx(b)],0.03)
setrgbcolor('red')
setdash('[2] 0')
line([c, 0], [c, fx(c)])
setdash('[] 0')
roundPoint([c, 0])
tangentSegment(c)
tangentSegment(c2)
setrgbcolor('black')
#annotations
annotate([-0.7, fx(-0.7)], [2,2], '$y=f(x)$')
annotate([a, fx(a)], [2,2], '$A$')
annotate([b, fx(b)], [-8, -8], '$B$')
annotate([a, 0], [-2, -12], '$a$')
annotate([b, 0], [-2, -12], '$b$')
annotate([c, 0], [-2, -12], '$c$')
closeOutputFile()


