#!/usr/bin/python
## Time-stamp : Thu Oct 11 21:51:04 CDT 2007 angenent
from grapher import *
from math import *

setViewBox(-0.2, -0.2, 2.2, 1.5 )
openOutputFile("04slidingPole",180)
A=[0, 0.7]
B=[1.1, 0]
C=[(A[0]+B[0])/2, (A[1]+B[1])/2]
#wall and floor
polygonA([[0,1], [0,0], [2,0]])

#ladder
linewidth(2)
setrgbcolor('midnight')
line(A, B)


linewidth(1.5)
setrgbcolor('red')
line(B, [B[0]+0.4, 0])
arrowhead(B, [B[0]+0.4, 0])
line(A, [0, A[1]-0.3])
arrowhead(A, [0, A[1]-0.3])
linewidth(1)

roundPoint(A)
roundPoint(B)
annotate(A, [3, 3], "$A$")
annotate(B, [2, 4], "$B$")
annotate(C, [2, 2], "\\sffamily pole of length 10 ft")
annotate([0, A[1]/2], [-18, 0], "$a(t)$")
annotate([B[0]/2, 0], [-4, -12], "$b(t)$")

closeOutputFile()
    

