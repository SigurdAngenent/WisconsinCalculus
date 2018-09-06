#!/usr/bin/python
# Time-stamp : Mon Nov 26 15:33:36 CST 2007 angenent

from  grapher  import *
from math import *

def x(h,z): return  0.6*(1-h*h)*cos(z)
def y(h,z): return  h+0.3*(1-h*h)*sin(z)
def Zfold(h):
    global htop, hbot
    return asin(-0.6*h)
def xtop(t) :
    global htop, hbot
    return x(htop, t)
def ytop(t) :
    global htop, hbot
    return y(htop, t)
def xbot(t) :
    global htop, hbot
    return x(hbot, t)
def ybot(t) :
    global htop, hbot
    return y(hbot, t)
def xside(h) : return x(h, Zfold(h))
def yside(h) : return y(h, Zfold(h))
def xotherside(h) : return x(h, pi-Zfold(h))
def yotherside(h) : return y(h, pi-Zfold(h))

setViewBox(-1.1,-1,3,1)
openOutputFile("09solid",180)

Nt=300
dt=2*pi/Nt
tees=[i*dt for i in range(Nt+1)]
hbot= -0.5
htop = 0.5

#draw the bottom
plot(xbot, ybot, 0, 2*pi)
# draw the sides
plot(xside, yside, hbot, htop)
plot(xotherside, yotherside, hbot, htop)
# draw the top
plot(xtop, ytop, 0, 2*pi)
closeOutputFile()


