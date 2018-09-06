#!/usr/bin/python
from grapher import *
from math import *
hoek = pi/6

setViewBox(-0.1, -0.1, 1.1, tan(hoek)+0.1)
openOutputFile("03dsin",180)


#the drawing
linewidth(2)
line([0.0, 0.0],[1.0, 0.0])
arc([0.0, 0.0], 1.0, [0, hoek*180/pi])
line([cos(hoek), sin(hoek)],[0,0])
linewidth(0.5)
	
line([1.0,tan(hoek)], [0.0, 0.0])
line([1.0, 0.0], [cos(hoek), sin(hoek)])
line([1.0, 0.0],[1.0, tan(hoek)])
setdash("[3] 0 ")
line([cos(hoek), 0.0], [cos(hoek), sin(hoek)])
setdash("[] 0 ")

linewidth(1)
roundPoint([0,0], 0.01)
roundPoint([1,0], 0.01)
roundPoint([1,tan(hoek)], 0.01)
roundPoint([cos(hoek),sin(hoek)], 0.01)

#annotations
annotate([0,0], [0, -12], "$O$")
annotate([1,0], [0, -12], "$A$")
annotate([1,tan(hoek)], [-3, 6], "$B$")
annotate([cos(hoek), sin(hoek)], [-3, 6], "$C$")
annotate([cos(0.7*hoek), sin(0.7*hoek)], [3,0], "$\\theta$")
annotate([1.0, 0.5*tan(hoek)], [4, -5], "\\rotatebox{90}{$\\tan\\theta$}")
annotate([cos(hoek), 0.5*sin(hoek)], [-10, -5], "\\rotatebox{90}{$\\sin\\theta$}")

closeOutputFile()


