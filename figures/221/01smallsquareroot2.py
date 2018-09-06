#!/usr/bin/python
# Time-stamp: Wed May 28 14:12:37 CDT 2008 angenent
import grapher
from math import *

grapher.ViewBox=[-1.1, -0.1, 1.1, 2.1]
grapher.openOutputFile("01smallsquareroot2",70)


grapher.linewidth(2)
grapher.polygonC([[0,0], [1,0], [1,1], [0,1]])
grapher.linewidth(0.5)
grapher.polygonC([[0,0], [1,1], [0,2], [-1,1]])
grapher.setdash("[3] 0")
grapher.polygonA([[0, 2], [0, 1], [-1,1]])
grapher.setdash("[] 0")


grapher.closeOutputFile()


