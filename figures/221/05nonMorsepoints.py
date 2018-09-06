
#!/usr/bin/python
## Time-stamp : Wed May 28 09:57:21 CDT 2008 angenent

from  grapher  import *
from math import *

def x(t): return t

setViewBox(-1,-1, 6, 1)
openOutputFile("05nonMorsepoints",280)


linewidth(0.25)
for z in [0, 2.5, 5]:
    arrow([z-1, 0], [z+1, 0], 5, 2, 0)
    arrow([z, -0.3], [z, 1], 5, 2, 0)
#    arrowhead([z-1, 0], [z+1, 0], 5, 2, overshoot=0)
#    arrowhead([z, -1], [z, 1], 5, 2, overshoot=0)

linewidth(2)
plot(x, (lambda t: t*t*t), -1, 1)
plot(x, (lambda t: (t-2.5)**4), 1.5, 3.5)
plot(x, (lambda t: -(t-5)**4), 4, 6)

setrgbcolor('red')
for z in [0, 2.5, 5]:
    linewidth(2)
    line([z-0.7,0], [z+0.7,0])
    linewidth(1)
    roundPoint([z,0],0.04)

annotate([0.2, 0.8],[0,0],"$y=x^3$")
annotate([2.7, 0.8],[0,0],"$y=x^4$")
annotate([5.2, 0.8],[0,0],"$y=-x^4$")
annotate([0, -0.3], [0, -12],
         makeboxc(r"""%
\parbox{60pt}{\centering%
neither min\\ nor max}"""))
annotate([2.5, -0.3], [0, -12],
         makeboxc(r"""local min"""))
annotate([5, -0.3], [0, -12],
         makeboxc(r"""local max"""))
closeOutputFile()


