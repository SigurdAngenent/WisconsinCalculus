#!/usr/bin/python
# Graph of powers of x, and some multiples of x
from math import *
from grapher import *


setViewBox(-0.2, -0.2, 1.2, 1.2)
openOutputFile("02powersOfx", 180)

axes()
linewidth(0.5)
plotfun((lambda x:x))
setrgbcolor('green')
plotfun((lambda x:x*x))
setrgbcolor('red')
plotfun((lambda x:x*x*x))
setrgbcolor('orange')
plotfun((lambda x:x*x*x*x))
setrgbcolor('blue')
plotfun((lambda x:x**10))
setrgbcolor('eggplant')
plotfun((lambda x:x**20))
setrgbcolor('black')

setdash("[3 3] 0")
line ([1, 0], [1, 1])
setdash("[] 0")

linewidth(1)
roundPoint([1, 0], 0.01)

annotate([1,0], [0, -9], makeboxc("$1$"))
annotate([0.5, 0.5], [-2, 2], makeboxr("$x$"))
annotate([0.65, 0.65**2], [-2, 2], makeboxr("$x^2$"))
annotate([0.7, 0.7**3], [1, -1], makeboxr("$x^3$"))
annotate([0.7, 0.7**4], [0, -4], makeboxl("$x^4$"))
annotate([0.8, 0.8**10], [3, 0], makeboxr("$x^{10}$"))
annotate([0.09**0.05, 0.09], [3, 0], makeboxl("$x^{20}$"))
closeOutputFile()


