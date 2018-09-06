#!/usr/bin/python
## Time-stamp : Thursday, September 6, 2007 2:32:42 PM
from grapher import *
from math import *


setViewBox(-1.2,-0.6, 1.2, 1.5)
openOutputFile("04sqrtNoTangent",90)

#the drawing
line([Viewxmin(),0], [Viewxmax(),0])
setrgbcolor([0,0,192])
linewidth(2)
plot((lambda t: t*t), (lambda t:t), 0,1)
plot((lambda t: -t*t), (lambda t:t), 0,1)
linewidth(0.5)
arrow([-0.8, 0.25], [-0.44, 0.6], 5, 1)

setrgbcolor([192,0,0]) 
linewidth(1)
line([0,Viewymin()], [0,Viewymax()])


setrgbcolor('black')
roundPoint([0,0], 0.05)

annotate([Viewxmin(),0], [0,4], "$y=\\surd{|x|}$")
annotate([0,0.7],[-8,0],\
        "\\rotatebox{90}{\\small\\sffamily\\itshape tangent? }")

closeOutputFile()
    

