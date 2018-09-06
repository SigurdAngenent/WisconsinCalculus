#!/usr/bin/python
# Leaky Bucket solution
from math import *
from grapher import *

def sqmin(x):
    if (x>0):
        return 0
    else:
        return x*x

setViewBox(-4, -1, 4, 4)
openOutputFile("04leakybucket-sltn", 240)

linewidth(0.5)
axes([7,7])
for x in [-3, -2, -1, 1, 2, 3]:
    line([x,0], [x, 0.05])
    PStext([x,0], [-2, -10], "%d"%(x), 'Helvetica-Narrow-Oblique')

for y in [1, 2, 3]:
    line([-0.05,y], [0.05,y])
    PStext([0,y], [2, -2], "%d"%(y), 'Helvetica-Narrow-Oblique')

PStext([3.5,0], [0, 4], 't', 'Helvetica-Narrow-Oblique')
PStext([0,3.8], [4, 0], 'h(t)', 'Helvetica-Narrow-Oblique')

colors = ['red', 'green', 'plum', 'tangerine']

linewidth(1)
for C in [-2, -1, 0, 1]:
    setrgbcolor(colors.pop())
    plot((lambda t:t), (lambda t: sqmin(t-C)), Viewxmin(), Viewxmax()-0.5)


    

closeOutputFile()


