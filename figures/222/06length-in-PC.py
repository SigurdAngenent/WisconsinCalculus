#!/usr/bin/python
# Solution to the right angle problem
from math import *
from grapher import *

setViewBox(-0.1, -0.2, 1, 2)
openOutputFile("06length-in-PC", 144)

def f(q): return q
def x(q): return f(q)*cos(q)
def y(q): return f(q)*sin(q)

q0=pi/3
q1=q0+0.2
r0=f(q0)
r1=f(q1)
r2=(r0+r1)/2
q2=(q0+q1)/2

axes([5,5])
linewidth(2)
line([r0*cos(q1), r0*sin(q1)],[r1*cos(q1), r1*sin(q1)])
arc([0,0], f(q0), [180*q0/pi, 180*q1/pi])
plot(x, y, q0,q1)
linewidth(0.5)
for q in (q0,q1):
    line([0,0], [r0*cos(q), r0*sin(q)])
plot(x, y, 0, pi/8)
plot(x, y, pi/6, q0)
plot(x, y, q1, pi/1.8)
linewidth(1)
arc([0,0], r0/2, [180*q0/pi, 180*q1/pi])


annotate([r2*cos(q1), r2*sin(q1)], [-1,0], makeboxr(r"$dr$"))
annotate([r0*cos(q2), r0*sin(q2)], [-1,-11], makeboxc(r"$rd\theta$"))
annotate([r0/2*cos(q1), r0/2*sin(q1)], [3,0], makeboxl(r"$d\theta$"))
annotate([f(pi/6)*cos(pi/6), f(pi/6)*sin(pi/6)],[0,-10],
        makeboxc(r"$r=f(\theta)$"))
annotate([r2*cos(q2), r2*sin(q2)], [2,0],
        makeboxl(r"$ds=\sqrt{(dr)^2+(rd\theta)^2}$"))
closeOutputFile()


