#!/usr/bin/python
# Time-stamp: <2012-07-31 11:17:54 angenent>  
#
from grapher import *
from math import *

def x(t): return t
def fx(t): return 0.2+(t-0.3)**2


setViewBox(<+xmin+>,<+ymin+>,<+xmax+>,<+ymax+>)
openOutputFile("<+drawingName+>",<+width+>)

axes()
plot(x, fx,  Viewxmin(), Viewxmax())

closeOutputFile()


