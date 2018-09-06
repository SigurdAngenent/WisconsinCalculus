#!/usr/bin/python
from math import *
from grapher import *

def linspace(a, b, n):  #{{{1
    dx=(b-a)/n
    return [a + k*dx for k in range(n+1)]
def constructpoint(t):  #{{{1
    A=[0,0]
    B=[t,1]
    C=[t, 1/(1+t*t)]
    D=[t/(1+t*t), 1/(1+t*t)]
    polygonA( [A,B,C,D] )
    roundPoint(C)
    PStext(B, [-4,1], 'Q', 'Helvetica-Oblique')
    PStext(C, [ 1,1], 'P', 'Helvetica-Oblique')
    if t>1:
        PStext(D, [-7,1], 'R', 'Helvetica-Oblique')
    else:
        PStext(D, [-9,-2], 'R', 'Helvetica-Oblique')

setViewBox(-1, -0.2, 5.2, 1.2)  #{{{1
openOutputFile("02Versiera", 360)

xx = linspace(0, 4.9, 100)
versiera = [ [x, 1/(1+x*x)]  for x in xx]
subversiera = [p for p in versiera]
subversiera.append([4.9, 0.0])
subversiera.append([0.0, 0.0])

polygonF(subversiera, "grey90")

setrgbcolor([0, 128, 255])
polygonA(versiera)
roundPoint([0,0.5], 0.5)

linewidth(0.25)
setrgbcolor('black')
x_axis(5)
y_axis(5)
line([-0.75,1], [4.5,1])
constructpoint(0.8)
constructpoint(2.0)
PStext([0,0], [-9, -9], 'O', 'Helvetica-Oblique')
closeOutputFile()

