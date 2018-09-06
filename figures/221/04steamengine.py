
#!/usr/bin/python
## Time-stamp: <2007-10-15 15:11:22 angenent>
from grapher import *
from math import *

setViewBox(-1.0, -1.2, 2.4, 1.2 )
openOutputFile("04steamengine",270)
O=[0,0]
A=[0.3, 0.4]
A1=[0.3-0.2, 0.4+0.15]
B=[2.0,0.0]
B1=[1.7,0]
roundPoint(O, radius=0.5)
line(A, B)
line(O, A)
x_axis()

setrgbcolor('red')
linewidth(2)
setlinecap(1)
line(B, B1)
line(A, A1)
arrowhead(B,B1, len=0.3, wid=0.15, overshoot=2)
arrowhead(A,A1, len=0.3, wid=0.15, overshoot=2)
setrgbcolor('black')

linewidth(1)
roundPoint(O, radius=0.02)
roundPoint(A, radius=0.02)
roundPoint(B, radius=0.02)

annotate(O, [-3, -12], "$O$")
annotate(A, [-2, 4], "$A$")
annotate(B, [-3, -12], "$B$")
annotate([0.2, 0.1], [0, 2], "$\\theta$")

closeOutputFile()
    

