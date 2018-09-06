#!/usr/bin/python
# Graph of e^x and first three Taylor polynomials.
from math import *
from grapher import *


setViewBox(-2.5, -0.75, 1.6, 4.0)
openOutputFile("02filltest", 240)

expsubgraph = [[0,0]]
expsubgraph.append([0,1])
expsubgraph.append([1,1])
expsubgraph.append([1,0])
expsubgraph.append([0,0])
polygonF(expsubgraph, 'chartreuse')
setrgbcolor([0,128,0])
polygonA(expsubgraph)
setrgbcolor('black')

closeOutputFile()


