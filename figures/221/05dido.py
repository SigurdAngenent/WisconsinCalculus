#!/usr/bin/python
## Time-stamp: Thu Oct 18 14:09:44 CDT 2007 angenent

from  grapher  import *
from math import *

setViewBox(-4,-0.1,4,2)
openOutputFile("05dido",180)

A=[-3,0]
B=[-3,1]
C=[-1,1]
D=[-1,0]

P=[0.5,0]
Q=[1.5,1.9]
R=[2.5,0]

linewidth(2)
line([-4, 0], [4, 0])
linewidth(1)

polygonF([A,B,C,D], fillcolor='gray')
polygonF([P,Q,R], fillcolor='gray')

for X in (A, B, C, D, P, Q, R):
    roundPoint(X)

annotate(A,[-8,3], "$A$")
annotate(B,[-8,3], "$B$")
annotate(C,[3,3], "$C$")
annotate(D,[3,3], "$D$")
annotate(P,[-6,3], "$P$")
annotate(Q,[3,3], "$Q$")
annotate(R,[3,3], "$R$")

annotate([3.5, 0], [0,3], "land")
annotate([3.5, 0], [0,-10], "water")

closeOutputFile()


