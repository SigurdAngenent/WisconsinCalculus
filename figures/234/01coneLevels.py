#!/usr/bin/python
# Cone or Paraboloid ?
from math import *
from grapher import *

setViewBox(-2, -2, 2, 2)
openOutputFile("01coneLevels", 120)
axes([5,5])

for r in (0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4):
    roundPoint([0,0], r, '', '')

closeOutputFile()


