#!/usr/bin/python
# level curves of the saddle function z=xy
from math import *
from grapher import *

def id(x): return x

setViewBox(-3, -2.2, 3, 2.2)
openOutputFile("01saddlelevels", 240)
axes([5,5])

linewidth(0.25)
for x in (-2, -1, 1, 2):
    line([x, -2.5], [x, 2.5])
    line([-2.5, x], [2.5, x])
linewidth(1)


for r in (0.2, 0.6, 1.0, 1.4):
    plot(id,lambda x: r/x, r/2, 2.5)
    annotate([2.5, r/2.5], [2,0],
            makeboxl("{\\footnotesize \\tt$xy=$%2.1f}"%(r)))
    plot(id,lambda x: r/x, -r/2, -2.5)
    annotate([-2.5, -r/2.5], [-2,-2],
            makeboxr("{\\footnotesize \\tt$xy=$%2.1f}"%(r)))



closeOutputFile()


