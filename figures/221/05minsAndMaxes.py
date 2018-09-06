#!/usr/bin/python
## Time-stamp: Mon Sep  3 14:58:50 CDT 2007 angenent

from  grapher  import *
from math import *

def locmin(bracket, f, eps=0.00001):
    a,b = bracket[0], bracket[1]
    c=0.5*(a+b)
    fa,fb,fc=f(a),f(b),f(c)
    if (fa<fc) or (fb<fc):
        print "failed to locate minimum"
        return
    while(b-a>eps):
        a1=(a+c)*0.5
        fa1=f(a1)
        if(fa1<fc):
            b, c = c, a1
            fb,fc=fc,fa1
            continue
        a2=(b+c)*0.5
        fa2=f(a2)
        if(fa2<fc):
            a, c = c, a2
            fa,fc=fc,fa2
            continue
        a, b = a1, a2
        fa,fb=fa1,fa2
    print "found max/min f(%lf)=%lf"%(c, f(c))
    return c
    

def x(t): return t
def fx(t): return t**4-t*0.3-0.5+exp(-6*(t+0.2)**2)

print fx(-1), fx(1)
#find the interior local min and maxima
p=locmin([-1,-0.2], fx)
q=locmin([-0.5,0.2], lambda t: -fx(t))
r=locmin([0,1], fx)

setViewBox(-1.2, -0.6, 1.2, 0.9)
openOutputFile("05minsAndMaxes",240)


linewidth(2)
#the domain
line([-1,0],[1,0])
#the graph
plot(x,fx, -1, 1)
#other lines
setdash("[2] 0")
linewidth(0.3)
line([Viewxmin(), 0], [-1,0])
line([1,0], [Viewxmax(),0])
line([-1,0],[-1,fx(-1)])
line([ 1,0],[ 1,fx( 1)])
setdash("[] 0")
linewidth(1)
roundPoint([-1, 0], 0.02)
roundPoint([1, 0], 0.02)
setrgbcolor('blue')
roundPoint([-1, fx(-1)], 0.02, fillcolor='blue')
roundPoint([1, fx(1)], 0.02, fillcolor='blue')
linewidth(2)
setrgbcolor('red')
for z in (p,q,r):
    fz=fx(z)
    line([z-0.15, fz],[z+0.15, fz])
    roundPoint([z, fz], 0.02)

#annotations
annotate([-1,0], [-2,-12], "$a$")
annotate([ 1,0], [-2,-12], "$b$")
annotate([-1,fx(-1)], [-12,6], r"{\footnotesize\sffamily\itshape abs max}")
annotate([ 1,fx( 1)], [-12,6], r"{\footnotesize\sffamily\itshape loc max}")
annotate([q, fx(q)], [-12,6], r"{\footnotesize\sffamily\itshape loc max}")
annotate([p, fx(p)], [-12,-8], r"{\footnotesize\sffamily\itshape loc min}")
annotate([r, fx(r)], [-12,-8], r"{\footnotesize\sffamily\itshape abs min}")
closeOutputFile()


