#!/usr/bin/python
# Cone or Paraboloid ?
from math import *
from grapher import *

OO  = [0,0]
E1 = [1.0, 0.0]
E2 = [0.0, 1.0]
alpha = pi/3
F1 = [cos(alpha), sin(alpha)]
F2 = [-sin(alpha), cos(alpha)]
halfE1= [0.5*x for x in E1]
halfE2= [0.5*x for x in E2]
halfF1= [0.5*x for x in F1]
halfF2= [0.5*x for x in F2]

setViewBox(-1.0, -0.5, 1.5, 1.5)
openOutputFile("01change-of-basis2", 240)
linewidth(0.3)
axes([0,0])
setrgbcolor("red")
arrow(OO,E1)
arrow(OO,E2)
setrgbcolor("aqua")
arrow(OO,F1)
arrow(OO,F2)
setrgbcolor("black")
roundPoint(OO, 0.02)

arc(OO, 0.3, [0.0, 180*alpha/pi])

annotate(halfE1, [0,-10], makeboxc( r"$\ves1$" ) )
annotate(halfE2, [-7,0], makeboxc( r"$\ves2$" ) )
annotate(halfF1, [-3,5], makeboxc( r"$\vfs1$" ) )
annotate(halfF2, [-6,-6], makeboxc( r"$\vfs2$" ) )
annotate([0.3*cos(alpha/2), 0.3*sin(alpha/2)], [1,1], makeboxl(r"$\alpha$") )
closeOutputFile()


