#!/usr/bin/python
# Time-stamp : Fri Nov 30 09:32:45 CST 2007 angenent
#
from  grapher  import *
from math import *



setViewBox(-0.5,-0.5,6.5,4)
openOutputFile("09bowl_variation2",270)

line([-0.25, 0], [2.25, 0])
line([0, -0.25], [0, 3])
plot(lambda x:1+x, lambda x:x*x, -1,1)
a=0.3
ya=(1-a)*(1-a)
b=1
# The axis of rotation
linewidth(2)
line([a, ya], [a, 1])
line([-0.5, 2], [2.5, 2])
annotate([1,2], [0,4], "Rotation axis")
linewidth(1)
C = [4.5, 2]
roundPoint(C, 2-ya, fillcolor='lightGray')
roundPoint(C, 1, fillcolor='white')
line(C, [C[0]+0.5*(2-ya), C[1]-0.5*sqrt(3)*(2-ya)])
line(C, [C[0]+0.5, C[1]+0.5*sqrt(3)])

setdash("[3] 0")
linewidth(0.5)
line([a, 0], [a, ya])
line([0, ya], [a, ya])
line([a,ya], [4.5,ya])
line([0,1], [4.5,1])
line([2.5, 2], C)
setdash("[] 0")
roundPoint([a,ya], 0.025, fillcolor='white')
roundPoint([a, 1], 0.025, fillcolor='white')
roundPoint(C, 0.025, fillcolor='white')


annotate([a, ya], [2, 4], "$A$")
annotate([a, 1], [-4, 4], "$B$")
annotate([a, 0], [-2, -10], "$x$")
annotate([C[0]+0.25*(2-ya), C[1]+0.25*sqrt(3)*(2-ya)], [2, -6],
    "$r_{\\mathrm{in}}$")
annotate([C[0]+0.3, C[1]-0.3*sqrt(3)], [2, 2], "$r_{\\mathrm{out}}$")
annotate([0, ya], [-36, -1], "$(1-x)^2$")
annotate([0, 1], [-7, -1], "1")
annotate([0, 2], [-7, 4], "2")
annotate([1, 0], [-2, -10], "1")
annotate([2, 0], [-2, -10], "2")
annotate([3.6, 0.2], [0,0],
    "Area$=\\pi r_{\\mathrm{out}}^2-\\pi r_{\\mathrm{in}}^2$")


closeOutputFile()


