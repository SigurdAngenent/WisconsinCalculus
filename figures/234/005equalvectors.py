#!/usr/bin/python
# equal vectors
from math import *
from grapher import *



setViewBox(-3, -2, 21, 12)
setTarget("png")
openOutputFile("005equalvectors", 120)
A=[0,0]
B=[5,7]
C=[12,3]
D=[17,10]

setrgbcolor('UWBadgerRed')
arrow(A,B)
arrow(C,D)
setrgbcolor('gray')
n=9
linewidth(0.3)
for i in range(1,n):
    arrow([i*12.0/n,i*(3.0/n)], [5+i*12.0/n,7+i*(3.0/n)], 7, 2)

annotate(A, [0, -10], makeboxc("$A$"))
annotate(B, [0,   2], makeboxc("$B$"))
annotate(C, [0, -10], makeboxc("$C$"))
annotate(D, [0,   2], makeboxc("$D$"))
closeOutputFile()


