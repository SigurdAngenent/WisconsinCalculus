from grapher import *
from math import *

def x(t): return t
def fx(t): return t*(t*t-3)

def tangentSegment(t, seglen=0.5):
    vx=1
    vy=3*t*t-3
    v=sqrt(vx*vx+vy*vy)
    vx, vy= vx/v, vy/v
    xx, yy = x(t), fx(t)
    line([xx- seglen*vx, yy-seglen*vy],\
         [xx+ seglen*vx, yy+seglen*vy])
    roundPoint([xx, yy], 0.05)

setViewBox(-4, -4, 4, 4)
openOutputFile("05upAndDown",270)

a=1.0

axes()

#the graph
linewidth(2)
setrgbcolor([255, 0, 0])
plot(x,fx, -3, -a)
setrgbcolor([0,0,  255])
plot(x,fx, -a, a)
setrgbcolor([255, 0, 0])
plot(x,fx, a, 3)

h = Viewymin()+1
setrgbcolor('white')
polygonF(rect(Viewxmin(), Viewxmax(), h-0.5, h-0.1),
         fillcolor='white')
polygonF(rect(-1.3, -0.3, -0.5, -0.05),
         fillcolor='white')
setrgbcolor('black')
setdash("[3] 0")
linewidth(0.5)
line([a, Viewymin()], [a, 0])
line([-a, Viewymin()], [-a, fx(-a)])
setdash("[] 0")
setrgbcolor('white')
polygonF(rect(-1.3, -0.3, -0.5, -0.05),
         fillcolor='white')
polygonF(rect(0.3, 1.3, -0.5, -0.05),
         fillcolor='white')
setrgbcolor('black')

linewidth(1)
tangentSegment(a, seglen=0.5)
tangentSegment(-a, seglen=0.5)

#regions
linewidth(0.5)

def region(a,b, h):
    h+=0.1
    line([a+0.02, h], [b-0.02, h])
    arrowhead([a+0.02, h], [b-0.02, h], 7)
    arrowhead([b-0.02, h], [a+0.02, h], 7)
region(Viewxmin(), -a, h)
region(-a, a, h)
region(a, Viewxmax()-0.02, h)
#annotations
annotate([(Viewxmin()-a)/2, h], [0, -10], makeboxc("$f'(x)>0$"))
annotate([(Viewxmax()+a)/2, h], [0, -10], makeboxc("$f'(x)>0$"))
annotate([0, h], [0,-10], makeboxc("$f'(x)<0$"))
annotate([ a, 0], [-12,-12], "$x=+1$")
annotate([-a, 0], [-12,-12], "$x=-1$")
annotate([-3, 3], [0,0], makeboxc(r"\framebox{$y=x^3-3x$}"))
line([-3, 2.8], [-1.3, fx(-1.3)])
closeOutputFile()


