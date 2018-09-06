#!/usr/bin/python
## Time-stamp : Wed May 28 11:20:37 CDT 2008 angenent
from grapher import *
from math import *

setViewBox(-1.2,-1.2, 1.2, 1.2)
openOutputFile("04absxNoTangent",90)

#the drawing
axes([5, 5])


linewidth(1)
setrgbcolor('red')

xx = 1.0
yy = 0.6*xx
line([-xx,-yy], [xx, yy])
annotate([-xx,-yy], [1,-6],
         rotatebox(atan(yy/xx)*180/pi, "{\\small\\sffamily\\itshape tangent?}"))

linewidth(2)
setrgbcolor('midnight')
polygonA([[-1,1], [0,0],[1,1]])
linewidth(1)
setrgbcolor([0,0,0])
annotate([-1,1], [0,5],makeboxc(r"$y=|x|$"))

closeOutputFile()
    

