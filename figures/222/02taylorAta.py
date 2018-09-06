#!/usr/bin/python

from math import *
from grapher import *

def id(t): return t
def f(t): return 1.0/(t*(5-t))

def polyeval(c, x):
    s,i=0,len(c)
    while(i>0):
        i-=1
        s = c[i]+s*x
    return s

def taylor(n,a):
    c=[]
    t1 = 0.2/a
    t2 = 0.2/(5.0-a)
    c.append(t1+t2)
    for i in range(n-1):
        t1/=(-a)
        t2/=(5.0-a)
        c.append(t1+t2)
    return(c)

a=1.0
b=4.5

setViewBox(-1, -4.0, 6, 4.0)
openOutputFile("02taylorAta", 240)

axes()
#linewidth(0.5)
plot(id, f, 0.02, 4.98)

linewidth(0.333)
setrgbcolor('red')
for k in [4,8,12,20]:
    Tat2= taylor(k,a)
    plotfun((lambda t: polyeval(Tat2, t-a)))
setdash("[2 2] 0")
line([a,0], [a, f(a)])
setdash("[] 0")
roundPoint([a, f(a)])

setrgbcolor('blue')
for k in [4,8,12,20]:
    Tat2= taylor(k,b)
    plotfun((lambda t: polyeval(Tat2, t-b)))
setdash("[2 2] 0")
line([b,0], [b, f(b)])
setdash("[] 0")
roundPoint([b, f(b)])

setrgbcolor('black')
setdash("[2 2] 0")
line([5,Viewymin()], [5, Viewymax()])
setdash("[] 0")

roundPoint([a,0])
roundPoint([b,0])
roundPoint([5,0])

annotate([a,0], [0, -9], makeboxc("$1$") )
annotate([b,0], [0, -9], makeboxc("$4.5$") )
annotate([5,0], [2, -9], makeboxl("$5$") )
annotate([2.5,2],[0,0], makeboxc(r"""$f(x) = \dfrac1{x(5-x)}$"""))
closeOutputFile()


