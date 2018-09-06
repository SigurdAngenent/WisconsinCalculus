#!/usr/bin/python
## Time-stamp : Fri Oct  5 16:37:42 CDT 2007 angenent

from  grapher  import *
from math import *

def x(t): return t
def fx(t): return 1/t


setViewBox(-4,-4, 4,4)
openOutputFile("05hyperbola", 150)
axes()

a=-1
b=1
fa=fx(a)
fb=fx(b)
A=[a,fa]
B=[b,fb]

#the graph
setrgbcolor([255, 0, 0])
plot(x,fx, -4, -0.25)
plot(x,fx, 0.25, 4)
setrgbcolor([0, 0, 0])

setdash("[2] 0")
linewidth(0.5)
polygonA([[a,0], A, [0, fa]])
polygonA([[b,0], B, [0, fb]])
setdash("[] 0")
roundPoint(A, radius=0.04)
roundPoint(B, radius=0.04)
roundPoint([a,0], radius=0.04)
roundPoint([b,0], radius=0.04)
#roundPoint([0, fa], radius=0.04)
#roundPoint([0, fb], radius=0.04)
arrowhead(A, [0,fa], 6, 2, -1)
arrowhead(B, [0,fb], 6, 2, -1)

#annotations
annotate([-0.5,-2], [-4,0], makeboxr("$f'(x)<0$") )
annotate([0.5, 2], [4,0], "$f'(x)<0$")
annotate([4.0, 0.0], [3, -3], "$x$")
annotate([a,0], [0,2], makeboxc("$-1$"))
annotate([b,0], [0,-10], makeboxc("$1$"))
annotate([0,fa], [2,0], makeboxl("$-1$"))
annotate([0,fb], [-2,0], makeboxr("$1$"))
annotate([0.5,-2], [0,0], makeboxl(r"""\
        \begin{minipage}[t]{100pt}\raggedright
            $f'(x)<0$ for all $x$\\
            but $f$ is not decreasing\\
            since $f(1) > f(-1)$!!
        \end{minipage}"""))

closeOutputFile()


