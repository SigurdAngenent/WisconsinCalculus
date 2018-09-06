#!/usr/bin/python
# Time-stamp : Fri Nov 30 15:28:00 CST 2007 angenent

from  grapher  import *
from math import *

def x(h,z): return  (0.6-0.2*h)*cos(z)
def y(h,z): return  h+(0.2-0.15*h)*sin(z)+0.01*sin(4*z)
def xa(h,z): return  2+0.1*cos(7*pi*h)+(0.6-0.2*h)*cos(z)

setViewBox(-1.1,-1,3,1)
openOutputFile("09Cavalieri",180)

Nh=50
dh=1.0/Nh
heights = [-0.5+i*dh for i in range(Nh+1)]
Nt=300
dt=2*pi/Nt
tees=[i*dt for i in range(Nt+1)]
h0=heights[Nh/2]
h1=heights[1+Nh/2]

#the two solids
linewidth(0.5)
for h in heights:
  curve=[[x(h, t), y(h, t)] for t in tees]
  polygonF(curve, fillcolor='white')
  polygonC(curve)
  curve=[[xa(h, t), y(h, t)] for t in tees]
  polygonF(curve, fillcolor='white')
  polygonC(curve)


closeOutputFile()


