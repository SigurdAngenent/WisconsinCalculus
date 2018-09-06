#!/usr/bin/python
##Time-stamp: Aug  4 17:11 05increasingtangent.py

from grapher import *
from math import *

def x(t): return t
def y(t): return t-t*t*0.5
def dy(t): return 1-t
def tangent(t):
    labels=['$A$', '$B$', '$C$', '$D$', '$E$']
    yt=y(t)
    m=dy(t)
    sqm = sqrt(1+m*m)
    wd = 1/sqm
    line([t-wd, yt-wd*m], [t+wd, yt+wd*m])
    roundPoint([t, yt], 0.05)
    annotate([t, yt], [8*m/sqm, -8/sqm] , makeboxc(labels[t+1]) )
#setViewBox, openOutputFile
setViewBox(-1.6, -3.0, 3.01, 1.0)
openOutputFile("05decreasingtangent", 90)


#the graph
linewidth(2)
setrgbcolor('gray')
plot(x,y, -1.5, 3)
linewidth(1)
setrgbcolor('blue')
for k in range(-1, 3):
    tangent(k)
#annotations
annotate([1,-1.4], [0,-14], makeboxc(r"\footnotesize $f'(x)$ decreasing") )
annotate([1,-1.4], [0,0], makeboxc(r"\footnotesize$f''(x)<0$") )
closeOutputFile()


