#!/usr/bin/python

from math import *
from grapher import *

def id(t): return t
def f(t): return exp(-1.0/t)

setViewBox(-2.5, -0.25, 3.5, 1.5)
openOutputFile("02nochemistry", 240)

axes([7,7])

plot(id, f, 0.001, Viewxmax())
line([Viewxmin(),0], [0, 0])

linewidth(0.25)
arrow([-0.4, 0.6], [-0.02, 0.03], len=5, wid=1.5, overshoot=0)
annotate([-0.5, 0.5], [0,0],
         makeboxr(r"""%
\parbox[b]{72pt}{\raggedright 
The Taylor series at this point does not converge to $f$}"""))

linewidth(0.5)
for i in [1, 2, 3]:
    roundPoint([i,0])
    annotate([i,0], [0, -9], makeboxc("$%d$"%(i)))

annotate([2,f(2)], [-1,1], makeboxr("$y=e^{-1/x}$"))
closeOutputFile()


