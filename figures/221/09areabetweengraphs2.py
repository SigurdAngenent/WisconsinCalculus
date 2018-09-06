#!/usr/bin/python
# Time-stamp : Mon Nov 26 10:11:02 CST 2007 angenent

from grapher import *
from math import *
##################################################
def id(t): return t
def f(x): return (2-x) * x * 0.5
def g(x): return exp(x/3)+(1-x/1.7)**2-0.6
##################################################
setViewBox(-0.1, -0.2, 2.5, 1.6)
openOutputFile("09areabetweengraphs2",150)

n=20
imarked = 14
a=0.2
b=1.7
linewidth(1.5)
plot(id, f, a, b)
plot(id, g, a, b)
line([a, f(a)], [a, g(a)])
line([b, f(b)], [b, g(b)])


linewidth(0.4)
setrgbcolor('black')
plot(id, f,  Viewxmin(), Viewxmax())
plot(id, g,  Viewxmin(), Viewxmax())

xp=[a + i*(b-a)/n for i in range(n+1)]
x_axis(5)
for i in range(n):
  strip = [[xp[i], f(xp[i])],
           [xp[i], g(xp[i])],
           [xp[i+1], g(xp[i+1])],
           [xp[i+1], f(xp[i+1])] ]
  if(i==imarked):
    polygonF(strip, fillcolor='gray')
  else:
    line(strip[0], strip[1])

linewidth(0.5)
setdash("[3] 0")
line([a,0], [a, f(a)])
line([b,0], [b, f(b)])
line([xp[imarked],0], [xp[imarked], f(xp[imarked])])
line([xp[imarked + 1],0], [xp[imarked + 1], f(xp[imarked + 1])])

xc=(xp[imarked]+xp[imarked+1])*0.5
setdash("[] 0")
linewidth(0.5)
line([xp[imarked],0], [xp[imarked]-0.08, -0.2])
line([xp[imarked+1],0], [xp[imarked+1]+0.08, -0.1])
line([xc-0.15,0.15], [xc, 0.15])
arrow([xc,0.15], [xc, 0.02], 5, 1)

roundPoint([a,0], 0.015)
roundPoint([b,0], 0.015)
roundPoint([xp[imarked],0], 0.015)
roundPoint([xp[imarked+1],0], 0.015)
roundPoint([xc, 0], 0.015)

annotate([a,0], [-2,-12], "$a$")
annotate([b,0], [-2,-12], "$b$")
annotate([xp[imarked],0], [-12,-18], "$x_{k-1}$")
annotate([xp[imarked],0], [4,-12], "$x_{k}$")
annotate([xc-0.3, 0], [0,8], "$c_{k}$")
closeOutputFile()


