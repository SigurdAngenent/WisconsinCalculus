
#!/usr/bin/python
# Time-stamp : Mon Dec  3 10:11:48 CST 2007 angenent
#
from  grapher  import *
from math import *

def x(t): return t
def y(t): return 0.7*(1-(1-t)**2)


setViewBox(-0.2,-0.2,1.2,0.9)
openOutputFile("09velocity",120)

t0=0.4
t1=0.8
x0, y0 = x(t0), y(t0)
x1, y1 = x(t1), y(t1)

axes([7,7])
plot(x, y,  -0.1, 1.1)
# an arrow
setrgbcolor('red')
line([x0, y0], [x1, y1])
polygonF([[x1-0.07, y1-0.08],
          [x1-0.1,  y1-0.02],
          [x1,      y1],
          [x1-0.07, y1-0.08]])
setrgbcolor('black')
polygonA([[x0, y0], [x1, y0], [x1, y1]])
linewidth(0.5)
setdash("[3] 0")
line([x0, 0], [x0, y0])
line([x1, 0], [x1, y1])
line([0, y0], [x0, y0])
line([0, y1], [x1, y1])
setdash("[] 0")

linewidth(1)

roundPoint([x0,y0], 0.015)
roundPoint([x1,y1], 0.015)
roundPoint([x0,0], 0.015)
roundPoint([x1,0], 0.015)
roundPoint([0,y0], 0.015)
roundPoint([0,y1], 0.015)

annotate([x0, 0], [-6, -10], "$x(t)$")
annotate([x1, 0], [-6, -10], "$x(t+\\Delta t)$")
annotate([0, y0], [-2, -3], makeboxr("$y(t)$"))
annotate([0, y1], [2, 4], "$y(t+\\Delta t)$")
annotate([(x0+x1)/2, y0], [-4, -10], "$\\Delta x$")
annotate([x1, (y0+y1)/2], [2, -2], "$\\Delta y$")
closeOutputFile()


