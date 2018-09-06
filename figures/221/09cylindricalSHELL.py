# Time-stamp: <2012-07-30 08:58:56 angenent>

from grapher import *
from math import *
################################################################################
Pmat=[[0.8, -0.1], [0.4, 0.2], [0, 1]]
def proj(X):  #linear projection of R^3 onto R^2 
    global Pmat
    x=sum([Pmat[i][0]*X[i] for i in range(3)])
    y=sum([Pmat[i][1]*X[i] for i in range(3)])
    return [x, y]
def drawdisc(h, r, color):
    angles=[2*k*pi/100 for k in range(101)]
    curve=[proj( [r*cos(q), r*sin(q), h] ) for q in angles]
    setrgbcolor(color)
    polygonF(curve)
    setrgbcolor('black')
    polygonA(curve)
################################################################################
#find fold angle
def bisect(f, a, b):
    eps=0.000001
    fa, fb = f(a), f(b)
    if(fa*fb >0):
        print "\n==========NO ZERO FOUND IN BISECT.==========\n"
        return 0
    while(b-a > eps):
        c=(a+b)*0.5
        fc=f(c)
        if(fa*fc<=0):
            b, fb=c, fc
        else:
            a, fa=c, fc
    return c
def DX(q):
    P = proj([-sin(q), cos(q), 0])
    return P[0]
Q1 = bisect(DX, -pi/2, pi/2)
Q2 = Q1+pi
print(Q1, Q2)
################################################################################

def pline(A, B): line(proj(A), proj(B))
# main
setViewBox(-0.7, -0.2, 1.0, 2.1)
openOutputFile("09cylindricalSHELL",120)

drawdisc(0, 0.6, 'gray')
drawdisc(0, 0.55, 'white')
linewidth(0.5)
pline([0,0,0], [0,0,1.5])
linewidth(1)
drawdisc(1.5, 0.6, 'gray')
drawdisc(1.5, 0.55, 'white')
pline([0.6*cos(Q1), 0.6*sin(Q1), 0],
        [0.6*cos(Q1), 0.6*sin(Q1), 1.5])
pline([0.6*cos(Q2), 0.6*sin(Q2), 0],
        [0.6*cos(Q2), 0.6*sin(Q2), 1.5])
linewidth(0.5)
pline([0.55*cos(Q1), 0.55*sin(Q1), 0],
        [0.55*cos(Q1), 0.55*sin(Q1), 1.5])
pline([0.55*cos(Q2), 0.55*sin(Q2), 0],
        [0.55*cos(Q2), 0.55*sin(Q2), 1.5])
pline([-1, 0, 0], [1, 0, 0])
pline([0, -1, 0], [0, 1, 0])
pline([0,0,1.5], [0,0,2])

pline([0,0,1.5], [1,0,1.5])
pline([1, 0, 0], [1, 0, 1.5])
arrow=[[0.95, 0, 0.15], [1, 0, 0], [1.05, 0, 0.15]]
polygonA(map(proj, arrow))
arrow=[[0.95, 0, 1.35], [1, 0, 1.5], [1.05, 0, 1.35]]
polygonA(map(proj, arrow))
arrow=[[0.15, 0.0, 1.47], [0, 0, 1.5], [0.15, 0.0, 1.53]]
polygonA(map(proj, arrow))
arrow=[[0.35, 0.0, 1.47], [0.55, 0, 1.5], [0.35, 0.0, 1.53]]
polygonA(map(proj, arrow))
annotate(proj([1,0,0.75]), [2,0], "$h$")
setrgbcolor('white')
roundPoint(proj([0, 0.6, 1.5]), 0.08)
annotate(proj([0.2, 0, 1.5]), [2,2], "$r$")
setrgbcolor('black')
pline([0.55, 0, 1.5], [0.55, 0.7, 1.5])
pline([0.6, 0, 1.5], [0.6, 0.7, 1.5])
annotate(proj([0.55, 0.7, 1.5]), [-2, 2], "$\\Delta r$")


closeOutputFile()
