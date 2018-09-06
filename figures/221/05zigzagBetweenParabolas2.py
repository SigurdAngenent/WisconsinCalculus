#!/usr/bin/python
## Time-stamp: Tue Sep  4 14:42:31 CDT 2007 angenent

from grapher import *
from math import *

def x(t): return t
def f(t): return 0.5*t+t*t*sin(pi/t)
def g(t): return t*(0.5+t)
def h(t): return t*(0.5-t)

def zoom(x0,x1, b0,b1, b2):
    mag = (b1-b0)/(x1-x0)
    xx = [x0 + k*(x1-x0)/100 for k in range(101)]
    f0 = f(xx[0])
    z = [ ( b0 + mag*(t-x0) ,  b2+mag*(f(t)-f0) ) for t in xx]
    zt = [ ( b0 + mag*(t-x0) ,  b2+mag*(g(t)-f0) ) for t in xx]
    zb = [ ( b0 + mag*(t-x0) ,  b2+mag*(h(t)-f0) ) for t in xx]
    polygonA(z)
    setdash("[2] 0")
    setrgbcolor([0,128,0])
    polygonA(zt)
    polygonA(zb)
    setdash("[] 0")
    setrgbcolor('black')
    linewidth(0.3)
    b3, b4 = b2-0.03, b2+0.2
    polygonA(rect(b0,b1,b3,b4))
    annotate([b0, b3], [0, -10],
             makeboxc(r"\texttt{\upshape\footnotesize %3.1g}"%(x0)) )
    annotate([b1, b3], [0, -10],
             makeboxc(r"\texttt{\upshape\footnotesize %3.1g}"%(x1)) )
    arrow([b1,b3], [x0, h(x0)+0.01], 7, 2)
    annotate([b0,b4], [0,12], makeboxl(r"""\parbox{76pt}{\footnotesize\sffamily 
magnification of the graphs near the origin}"""))

setViewBox(-0.6,-0.6, 0.6, 0.6)
openOutputFile("05zigzagBetweenParabolas2",300)

axes()

#tangent at origin
linewidth(0.5)
line([-0.6,-0.3], [0.6, 0.3])
linewidth(1)
#upper and lower parabolas
setdash("[2] 0")
setrgbcolor([0,128,0])
plot(x,g, -0.6, 0.6)
plot(x,h, -0.6, 0.6)
setdash("[] 0")
#the graph of f
setrgbcolor([0,0,128])
plot(x,f, -0.6, -0.001)
plot(x,f, 0.001, 0.6)
setrgbcolor('black')

zoom(0.005, 0.006, -0.5, -0.2, 0.3)

for k in range(2,10):
    roundPoint([1.0/k, 0.5/k], 0.04/(k+2))

#annotations
annotate([0.5, g(0.5)], [4,0],"$y=\\frac 12x+x^2$")
annotate([Viewxmax(), h(Viewxmax())], [4,-3],"$y=\\frac 12x-x^2$")
annotate([0.6, 0.3], [3,0], "$y=\\frac 12x$")
annotate([0.55, f(0.55)], [2, 2], "$y=\\frac 12x+x^2\\sin\\frac\\pi x$")
closeOutputFile()


