#!/usr/bin/python
# Time-stamp : Sunday, November 18, 2007 4:19:24 PM
from grapher  import *
from math import *
from random import *

def x(t): return t
def fx(t): return 1/(1+(2*t-1)**2)

def makeframe(n, xp):
    dx = (xp[-1] - xp[0])/n
    xvals = [xp[0] + i*dx for i in range(n+1)]
    fr = [ (xx, fx(xx)) for xx in xvals]
    fr.append((xp[-1], 0))
    fr.append((xp[ 0], 0))
    fr.append(fr[0])
    return fr

setViewBox(-0.3,-0.1,2.3,1.5)
openOutputFile("08Riemann",300)

xp = (0.0, 0.3, 0.7, 1.0, 1.25, 1.6, 2.0)
n=len(xp)-1
c=[(4*uniform(xp[i],xp[i+1]) + xp[i] + xp[i+1])/6 for i in range(n)]
fxc = [fx(t) for t in c]

# the outer parts of the graph
plot(x, fx, Viewxmin(), xp[0])
plot(x, fx, xp[n], Viewxmax())

# the region whose area we want to know
fr = makeframe(100, xp)
polygonF(fr, [202,220,220])
setrgbcolor('blue')
linewidth(2)
polygonC(fr)
#
setrgbcolor('black')
linewidth(1)
x_axis()
#Heights at which the x_i and c_i labels will appear
xheight = -12
cheight = -24
linewidth(0.5)
annotate([xp[0], 0], [0, xheight], makeboxr("$a=x_0$"))

for i in range(n):
  polygonC( rect(xp[i], xp[i+1], 0,  fxc[i]) )
setdash("[2] 0")
setrgbcolor('plum')
for i in range(n):
  line([c[i], -0.12], [c[i], fxc[i]])
setdash("[] 0")
setrgbcolor('black')
for i in range(n):
  annotate([c[i], 0], [0, cheight], makeboxc("$c_%d$"%(i+1)))
  if (i<n-1):
      annotate([xp[i+1], 0], [0, xheight], makeboxc("$x_%d$"%(i+1)))
  else:
      annotate([xp[i+1], 0], [0, xheight], makeboxl("$b=x_%d$"%(i+1)))
  roundPoint([xp[i+1],0], radius=0.02, annotation='', fillcolor=[128,128,128])
  roundPoint([c[i],0], radius=0.02)
  roundPoint([c[i],fxc[i]], radius=0.02)
roundPoint([xp[0],0], radius=0.02, fillcolor=[128,128,128])


closeOutputFile()


