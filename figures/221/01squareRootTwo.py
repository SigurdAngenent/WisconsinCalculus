#!/usr/bin/python
# Time-stamp: < Sun Jul 29 12:14:50 CEST 2007>
import grapher
from math import *

grapher.ViewBox=[-0.5, -0.5, 2.5, 2.5]
grapher.openOutputFile("01squareRootTwo",180)

grapher.polygonC([[0,0], [2,0], [2,2], [0,2]])
grapher.polygonC([[1,0], [2,1], [1,2], [0,1]])
grapher.setdash("[3] 0")
grapher.line([1, 0], [1, 2])
grapher.line([0, 1], [2, 1])
grapher.setdash("[] 0")

grapher.annotate([0,0], [-3,-12], "$A$")
grapher.annotate([2,0], [-3,-12], "$B$")
grapher.annotate([2,2], [-3,  4], "$C$")
grapher.annotate([0,2], [-3,  4], "$D$")
grapher.annotate([1,0], [-3,-12], "$P$")
grapher.annotate([2,1], [4,  -4], "$Q$")
grapher.annotate([1,2], [-3,  4], "$R$")
grapher.annotate([0,1], [-12,-4], "$S$")

grapher.closeOutputFile()


