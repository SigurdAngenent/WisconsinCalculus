#!/usr/bin/python
# Graph of powers of x, and some multiples of x
from math import *
from grapher import *


setViewBox(-0.2, -0.2, 1.2, 1.2)
openOutputFile("02powerBeatsLinear", 180)

n=100
dx = 1.0/n
xx=[k*dx for k in range(n+1)]
parabola = [(x, x*x) for x in xx]
parabola.append( (1.0, 0) )
parabola.append( (0, 0) )
setrgbcolor( 'navajowhite' )
polygonF(parabola)

setrgbcolor( 'black' )
axes()
linewidth(0.5)
plotfun((lambda x:x))

setdash("[2 1] 0")
plotfun((lambda x:x/2))
plotfun((lambda x:x/5))
plotfun((lambda x:x/10))
plotfun((lambda x:x/20))

annotate([1.2, 1.2], [2, 0], makeboxl("$y=x$"))
annotate([1.2, 1.2/2], [2, 0], makeboxl("$y=x/2$"))
annotate([1.2, 1.2/5], [2, 0], makeboxl("$y=x/5$"))
annotate([1.2, 1.2/10], [2, 0], makeboxl("$y=x/10$"))
annotate([1.2, 1.2/20], [2, -3], makeboxl("$y=x/20$"))
annotate([0.9, 0.81], [5,0], makeboxl("$y=x^2$"))

closeOutputFile()


