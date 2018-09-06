#!/usr/bin/python
# Time-stamp : Sunday, November 18, 2007 4:19:24 PM
from grapher  import *
from math import *
from random import *

def x(t): return t
def fx(t): return 1/(1+2*t*t)


setViewBox(-0.3,-0.1,2.3,1.5)
openOutputFile("04Riemann1D",150)

xp = (0.0, 0.3, 0.7, 1.0, 1.25, 1.6, 2.0)
n=len(xp)-1
c=[(4*uniform(xp[i],xp[i+1]) + xp[i] + xp[i+1])/6 for i in range(n)]

plot(x, fx, Viewxmin(), xp[0])
plot(x, fx, xp[n], Viewxmax())

#setrgbcolor('blue')
#linewidth(2)
plot(x, fx,  xp[0], xp[n])
for x in (xp[0], xp[n]):
  line([x,0], [x, fx(x)])
line([xp[0],0], [xp[n],0])
#setrgbcolor('black')
linewidth(1)
x_axis()

#Height at which the x_i  will appear
xheight = -10
linewidth(0.5)
annotate([xp[0], 0], [0, xheight], makeboxr("$a=x_0$"))
roundPoint([xp[0],0], radius=0.02, fillcolor='black')
for i in range(n):
  y = fx(c[i])
  polygonC([[xp[i], 0], [xp[i+1], 0], [xp[i+1], y], [xp[i], y]])
  setdash("[2] 0")
  #setrgbcolor('plum')
  line([c[i], 0.0], [c[i], y])
  setdash("[] 0")
  #setrgbcolor('black')
  #annotate([c[i], 0], [0, cheight], makeboxc("$\\xi_%d$"%(i+1)))
  if (i<n-1):
      annotate([xp[i+1], 0], [2, xheight], makeboxc("$x_%d$"%(i+1)))
  else:
      annotate([xp[i+1], 0], [0, xheight], makeboxl("$b=x_%d$"%(i+1)))
  roundPoint([xp[i+1],0], radius=0.02, annotation='', fillcolor='black')
  roundPoint([c[i],0], radius=0.02)
  roundPoint([c[i],y], radius=0.02)



closeOutputFile()


