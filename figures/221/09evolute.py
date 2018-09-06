#!/usr/bin/python
# Time-stamp : Thu Dec  6 12:32:51 CST 2007 angenent
#
from grapher import *
from math import *

def evx(t):  #{{{1
    return cos(t)+t*sin(t)

def evy(t):  #{{{1
    return sin(t)-t*cos(t)

#{{{1  main
setViewBox(-5.1,-6.3,1.6,3.2)
openOutputFile("09evolute",360)

linewidth(0.25)
axes()
linewidth(1)
plot(cos, sin, 0, 2*pi)
plot(evx, evy, 0, 2*pi)
N=32
for k in range(N+1):
    t = 2*k*(pi/N)
    line([cos(t), sin(t)],  [evx(t), evy(t)])

closeOutputFile()


