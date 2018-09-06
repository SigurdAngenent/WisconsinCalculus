
#!/usr/bin/python
## Time-stamp: Tue Oct 16 11:41:21 CDT 2007 angenent

from  grapher  import *
from math import *

def x(t): return t
def fx(t): return t**5/5.0+t

def tangentSegment(t, seglen=0.5):
    vx=1
    vy=t**4+1
    v=sqrt(vx*vx+vy*vy)
    vx, vy= vx/v, vy/v
    xx, yy = x(t), fx(t)
    line([xx- seglen*vx, yy-seglen*vy],\
         [xx+ seglen*vx, yy+seglen*vy])
    roundPoint([xx, yy], 0.03)

setViewBox(-0.5,-0.5, 2.0,2.0)
openOutputFile("05mvt",180)

a = 0.2
b = 1.2
m = (fx(b)-fx(a))/(b-a)
c = (m-1)**(0.25)

axes()
linewidth(2)
plot(x, fx,  Viewxmin(), Viewxmax())
linewidth(1)

setdash('[2] 0')
setrgbcolor('blue')
line([a, 0], [a, fx(a)])
line([b, 0], [b, fx(b)])
roundPoint([a, 0])
roundPoint([b, 0])
setdash('[] 0')

line([a, fx(a)], [b, fx(b)])
roundPoint([a, fx(a)])
roundPoint([b, fx(b)])
setrgbcolor('red')
setdash('[2] 0')
line([c, 0], [c, fx(c)])
setdash('[] 0')
roundPoint([c, 0])
tangentSegment(c)
setrgbcolor('black')
#annotations
annotate([a, 0], [-2, -12], '$a$')
annotate([b, 0], [-2, -12], '$b$')
annotate([c, 0], [-2, -12], '$c$')
closeOutputFile()


