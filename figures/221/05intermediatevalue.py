#!/usr/bin/python
# Time-stamp : Thu Jun  5 16:21:22 CDT 2008 angenent
#
from grapher import *
from math import *

def x(t):
    return t
def fx(t):
    return 0.4*(1.5 + cos(pi*t))+peak(5*t-2)+0.04*sin(10*pi*t)+0.02*sin(13*pi*t)
def peak(t):
    return t*exp(-t*t)
def bisect(f,level, a, b):
  eps=0.000001
  fa, fb = f(a)-level, f(b)-level
  if(fa*fb >0):
    print "\n==========NO ZERO FOUND IN BISECT.==========\n"
    return 0
  while(b-a > eps):
    c=(a+b)*0.5
    fc=f(c)-level
    if(fa*fc<=0):
      b, fb=c, fc
    else:
      a, fa=c, fc
  return c


a=0.1
b=1.2
fa=fx(a)
fb=fx(b)
y = (2*fa+fb)/3

#find c values
print "........Computing c values"
clist=[]
dx = (b-a)/20
p,q = a, a+dx
fp, fq = fx(p)-y, fx(q)-y
while(p<b):
    if ((fp*fq) < 0):
        c=bisect(fx, y, p, q)
        clist.append(c)
    p,q = q, q+dx
    fp, fq = fq, fx(q)-y
print "........Found these:\n", clist

setViewBox(-0.1,-0.1,1.5,1.1)
openOutputFile("05intermediatevalue",180)

axes()
plot(x, fx,  a, b)
setdash("[1 2 3 2 3 1 2 3 4 2 3] 0")
linewidth(0.5)
line([0, y], [Viewxmax(), y])
line([0, fa], [a, fa])
line([0, fb], [b, fb])
for c in clist+[a,b]:
    fc=fx(c)
    setdash("[2] 0")
    line([c,0], [c, fc])
    setdash("[] 0")
    roundPoint([c,fc], 0.01)
    roundPoint([c,0], 0.01)

j=0
for c in clist:
    j+=1
    annotate([c,0], [0,-8], makeboxl("$c_%d$"%(j)) )
annotate([a,0], [0,-8], makeboxc("$a$") )
annotate([b,0], [0,-8], makeboxc("$b$") )
annotate([0,y], [-2,0], makeboxr("$y$") )
annotate([0,fa], [-2,0], makeboxr("$f(a)$") )
annotate([0,fb], [-2,0], makeboxr("$f(b)$") )
closeOutputFile()


