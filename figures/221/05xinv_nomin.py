

#!/usr/bin/python
## Time-stamp : Fri Oct  5 16:37:42 CDT 2007 angenent

from  grapher  import *
from math import *

def x(t): return t
def fx(t): return 1.0/(t*t)

setViewBox(-0.2, -0.2, 5, 1.2)
openOutputFile("05xinv_nomin", 235)
axes()

#the graph
setdash("[4] 0")
polygonA([[1,0], [1,1], [0,1]])
setdash("[] 0")
linewidth(1)
plot(x, fx, 1, 3)
setdash("[2 3] 0")
plot(x, fx, 3, 4.5)
setdash("[] 0")
roundPoint([1,1], 0.04, fillcolor='black')


#annotations
annotate([1,0], [-2, -12], "1")
annotate([0,1], [-12, -4], "1")
annotate([2, 0.25], [0, 4], makeboxl("$y=1/x^2$") )
annotate([1,1], [3, 4], makeboxc("max") )
annotate([4.5,0.1], [0, 0], makeboxc("min?") )
closeOutputFile()


