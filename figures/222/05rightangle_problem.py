#!/usr/bin/python
# Solution to the right angle problem
from math import *
from grapher import *

A = [1,1]
B = [3,2]
def C(t): return [t, 3-t]
M = [2, 1.5]

setViewBox(-1, -3, 6, 4)
openOutputFile("05rightangle-problem", 300)
axes([5,5])
linewidth(0.5)
for x in range(1,6):
    line([x,-0.05], [x,0.05])
for y in range(-4,4):
    line([-0.05,y], [0.05,y])
line(A, C(0))
line(B, C(5))
line(A,B)
line(C(0), B)
line(C(5), A)
polygonA([A,C(1),B,C(2.5),A])
line(C(-0.95), C(5.95))
setrgbcolor('blue')
arc(M, sqrt(1.25), [0,360])
setrgbcolor('black')
roundPoint(A)
roundPoint(B)
for t in (0, 1, 2.5, 5):
    roundPoint(C(t))

PStext(A, [-24,-10], "A(1,1)", "Palatino-Italic",7)
PStext(B, [2,2], "B(1,1)", "Palatino-Italic",7)
for t in (0,5):
    PStext(C(t), [2,2], "C (t=%d)"%(t), "Palatino-Italic", 7)

PStext(C(1), [4,2], "C (t=%2.1f)"%(1), "Palatino-Italic", 7)
PStext(C(2.5), [4,-3], "C (t=%2.1f)"%(2.5), "Palatino-Italic", 7)
closeOutputFile()


