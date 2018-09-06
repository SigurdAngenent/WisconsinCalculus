#!/usr/bin/python
# Time-stamp: <2012-07-29 11:03:44 angenent>

from grapher import *
from math import *

def x(h,z): return  0.3*h*h+(0.6-0.2*h)*cos(z)
def y(h,z): return  h+(0.3-0.2*h)*sin(z)+0.05*sin(4*z)

setViewBox(-1.1,-1,3,1)
openOutputFile("09Xsections",270)

Nh=30
dh=1.0/Nh
heights = [-0.5+i*dh for i in range(Nh+1)]
Nt=300
dt=2*pi/Nt
tees=[i*dt for i in range(Nt+1)]
h0=heights[Nh/2]
h1=heights[1+Nh/2]


for h in heights:
    curve=[[x(h, t), y(h, t)] for t in tees]
    polygonF(curve, fillcolor='white')
    polygonC(curve)

linewidth(2)
line([-1,-1], [-1, 1])
setdash("[3] 0")
linewidth(0.5)
for h in [heights[0], h0, h1, heights[Nh]]:
    line([x(h, 0), y(h, 0)], [2+x(h, 0), y(h, 0)] )
for h in [heights[0], h0, heights[Nh]]:
    line([x(h, pi), y(h, pi)], [-1, y(h, pi)] )
setdash("[] 0")
linewidth(1)

for h in [heights[0], h0, heights[Nh]]:
    roundPoint([-1, y(h, pi)])
annotate([-1, y(heights[0], pi)], [-10, -2], "$a$")
annotate([-1, y(h0, pi)], [-10, -2], "$x$")
annotate([-1, y(heights[Nh], pi)], [-10, -2], "$b$")

for [h, color] in [[heights[0], 'white'],
                   [h0, 'black'],
                   [h1, 'white'],
                   [heights[Nh],'white']]:
    curve=[[2+x(h, t), y(h, t)] for t in tees]
    polygonF(curve, fillcolor=color)
    polygonC(curve)

annotate([2+x(h0, 0), y(h0,0)], [2, -4], "Slice at height $x$")
annotate([2, y(h1,0)], [-24, -4], "Area $= A(x)$")
closeOutputFile()


