#!/usr/bin/python   {{{1
#The onion region

from math import *
from grapher import *

setViewBox(-0.5, -1, 1.3, 1)  #{{{1
openOutputFile("03onion", 120)

def P(t): #{{{1
    x=1/(1.0+t*t*0.25)
    return [x, t*x*x]

print( P(2/sqrt(3.0)) )

#{{{1 main
tees = [0.02 * i for i in range(-200,201)]
curve = [P(abs(t)*t) for t in tees]
polygonF(curve, 'gray')
polygonA(curve)
axes([7,7])

roundPoint([1,0], 0.02)
roundPoint([0.75, 0.375*sqrt(3)], 0.02)
roundPoint([0.75, -0.375*sqrt(3)], 0.02)
annotate([1,0], [2,2], makeboxl(r"$1$"))
annotate([0.75, 0.375*sqrt(3)], [0,7],
         makeboxc(r"$(\frac34, \frac38\sqrt3)$"))
annotate([0.75, -0.375*sqrt(3)], [0,-12],
         makeboxc(r"$(\frac34, -\frac38\sqrt3)$"))

closeOutputFile()


