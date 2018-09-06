#!/usr/bin/python
## Time-stamp : Fri Oct  5 16:37:42 CDT 2007 angenent

from  grapher  import *
from math import *



setViewBox(-0.2, -0.2, 1.2, 1.1)
openOutputFile("05xnomax", 100)
axes()

#the graph
linewidth(0.5)
setdash("[2] 0")
line([1,0], [1,1])
setdash("[] 0")
linewidth(2)
line([0,0], [1,1])
linewidth(1)
roundPoint([0,0], 0.03, fillcolor='black')
roundPoint([1,0], 0.03, fillcolor='black')
roundPoint([1,1], 0.03)


#annotations
annotate([1, 0 ], [0, -12], "$1$")
annotate([1,0], [-2, 4], makeboxr("$f(1)=0$") )
annotate([0, 0], [-2, 2], makeboxr("min") )
annotate([1, 1], [5, 0], makeboxl("max?") )

closeOutputFile()


