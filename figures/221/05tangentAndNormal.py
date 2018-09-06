#!/usr/bin/python
## Time-stamp: <2012-07-19 16:28:25 angenent>

from grapher import *
from math import *

def x(t): return t
def fx(t): return 1.8 - 1/t

setViewBox(-0.1,-0.1, 3.0,1.8)
openOutputFile("05tangentAndNormal",180)

axes([5,5])


linewidth(0.5)

#tangent and normal segments
seglen=0.9
t=1.2
vx, vy = 1, 1.0/(t*t)
angle=atan(vy)*180/pi
v=sqrt(vx*vx+vy*vy)
vx, vy= seglen*vx/v, seglen*vy/v
xx, yy = x(t), fx(t)
# where the normal hits the x-axis
xn = xx + yy*vy/vx
polygonF(rect(xn-0.05, xn+0.2, -0.1, 0.1), 'white')
#draw tangent and normal
line([xx- 2*vx, yy-2*vy], [xx+ 2*vx, yy+2*vy])
line([xx+ 2*vy, yy-2*vx], [xx- 2*vy, yy+2*vx])

#the windmill
setViewBox
linewidth(2)
setrgbcolor('black')
polygonF([[xx+ vy, yy-vx],\
          [xx, yy-vx],\
          [xx, yy],\
          [xx+ vy, yy-vx]], 'cyan')
polygonF([[xx, yy],
          [xx+ vx, yy],
          [xx+ vx, yy+vy],
          [xx, yy]], 'cyan')

polygonA([[xx+ vy, yy-vx],\
          [xx, yy-vx],\
          [xx, yy],\
          [xx+ vx, yy],\
          [xx+ vx, yy+vy]])
setrgbcolor('black')
#the graph
linewidth(1)
plot(x,fx, 0.3333, 2.8)
roundPoint([xx, yy], 0.03)

#annotations
annotate([3.0, 0.0], [2, -2], "$x$")
annotate([0.0, 1.8], [-2, 4], "$y$")
annotate([xx, yy-0.5*vx], [-15, -3], "$-1$")
annotate([xx+0.5*vy, yy-vx], [-4, -8], "$m$")
annotate([xx+0.5*vx, yy], [-2, -8], "$1$")
annotate([xx+vx, yy+vy/2], [2, -3], "$m$")
annotate([xx+0.4*vx, yy+0.4*vy], [-8, 0], 
        r"\rotatebox{%f}{\footnotesize slope $=m/1=m$}"%(angle))
annotate([xx+0.4*vy, yy-0.4*vx], [1, 3], 
        r"\rotatebox{%f}{\footnotesize slope $=-1/m$}"%(angle-90))

closeOutputFile()


