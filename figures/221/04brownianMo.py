#!/usr/bin/python
## Time-stamp: <2012-07-14 10:16:22 angenent>
from grapher import *
from math import *
from random import random, seed

def inset(p):
    global tinset, texpand, xinset, xexpand, xlo, xhi
    return [1.3+(p[0]-tinset)*texpand,
            xlo+(p[1]-xinset)*xexpand]

#Compute a Random Walk
seed(13)
N=80000
Nin0, Nin1 = 20000, 20500
x,t = 0,0
xlo,xhi=0,0
dt=4.0/N
dx=sqrt(dt)
bpath = [[0,0]]
for i in range(N):
    t=t+dt
    x=x+dx*(2*random()-1)
    if(x<xlo): xlo=x
    elif(x>xhi): xhi=x
    bpath.append([t, x])


setViewBox(-0.2, xlo-0.01, 4, xhi+0.01)
openOutputFile("04brownianMo",360)
axes([5,5])

#draw the inset
linewidth(0.5) 
tinset = bpath[Nin0][0]
texpand = 1.0/(bpath[Nin1][0]-tinset)
xinset = min([bpath[i][1] for i in range(Nin0, Nin1+1)])
xinsetmax = max([bpath[i][1] for i in range(Nin0, Nin1+1)])
xexpand = 0.5/(xinsetmax - xinset)
R = rect(bpath[Nin0][0], bpath[Nin1+1][0], xinset, xinsetmax)
iR1=inset(R[1])
arrow(R[3], iR1, 7, 2)
linewidth(1)
polygonA(R)
polygonF(R, 'yellow')
polygonA( map(inset, R) )

#Draw the Brownian Motions
setrgbcolor([192,0,0])
linewidth(0.5)
polygonA( map(inset, bpath[Nin0:Nin1+1]) )
linewidth(0.1)
polygonA(bpath[0:-1:10])

M=[ (R[3][0]+ iR1[0])/2, (R[3][1]+iR1[1])/2 ]
annotate(M, [1,1], makeboxl(r"{\rmfamily\itshape\footnotesize(magnify)}"))
annotate([3.95, 0], [0, 4], "$t$")
annotate([0.0, xhi-0.05], [5, 0], "$x(t)$")

print xlo, xhi
closeOutputFile()


