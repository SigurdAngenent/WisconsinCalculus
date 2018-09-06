# Time-stamp : Fri Nov 30 21:47:16 CST 2007 angenent

from  grapher  import *
from math import *
Pmat=[]
def unitize(x):
    l=sqrt( sum([t*t for t in x]) )
    return [t/l for t in x]
def make_Pmat(viewp):
    """Orthogonal projection along the vector viewp"""
    global Pmat
    a = unitize( [-viewp[1], viewp[0], 0] )
    b = unitize( [-viewp[2]*viewp[0],
                  -viewp[2]*viewp[1], 
                  viewp[0]**2 + viewp[1]**2] )
    Pmat = zip(a,b)
def proj(X):  #linear projection of R^3 onto R^2 
    global Pmat
    x=sum([Pmat[i][0]*X[i] for i in range(3)])
    y=sum([Pmat[i][1]*X[i] for i in range(3)])
    return [x, y]
def pline(A, B):
    line(proj(A), proj(B))
def jac(X, u, v):
    eps = 0.000001
    A = map( lambda p,q: (p-q)/eps,  X(u+eps/2, v), X(u-eps/2, v) )
    B = map( lambda p,q: (p-q)/eps,  X(u, v+eps/2), X(u, v-eps/2) )
    return A[0]*B[1]-A[1]*B[0]
def fold(r, thetamin, thetamax):
    return bisect(lambda theta:jac(psurf, r, theta), thetamin, thetamax)
def f(x):
    return exp(-x)
def surf(r, theta):
    return [r*cos(theta), r*sin(theta), f(r)]
def psurf(r,theta):
    return proj(surf(r,theta))
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
def drawdisc(h, r, color):
    angles=[2*k*pi/100 for k in range(101)]
    curve=[proj( [r*cos(q), r*sin(q), h] ) for q in angles]
    setrgbcolor(color)
    polygonF(curve)
    setrgbcolor('black')
    polygonA(curve)
#main  setViewBox, openOutputFile.
setViewBox(-1.2, -0.5, 1.2, 1.3)
openOutputFile("09solidWITHmanyshells",150)
# decide on a projection
make_Pmat([2,-3,0.75])

#find cylinderfold angle :
Q1 = bisect(DX, -pi/2, pi/2)
Q2 = Q1+pi
print(Q1, Q2)
#find right and left folds
print "looking for right folds"
xx = [0.02*k for k in range(51)]
RF = [(x, fold(x, -pi/2, pi/2)) for x in xx]
print "looking for left folds"
LF = [(x, fold(x, pi/2, 3*pi/2)) for x in xx]
# draw the base and side of the solid
drawdisc(0, 1, 'white')
drawdisc(f(1.0), 1, 'white')
drawdisc(0, 0.6, 'gray')
drawdisc(0, 0.55, 'white')
linewidth(0.5)
pline([0,0,0], [0,0,f(0.55)])
linewidth(1)
pline([cos(Q1), sin(Q1), 0],
      [cos(Q1), sin(Q1), f(1)])
pline([cos(Q2), sin(Q2), 0],
      [cos(Q2), sin(Q2), f(1)])
radii = [k*0.05 for k in range(20)]
radii.reverse()
for r in radii:
    drawdisc(f(r), r, 'white')
# draw the folds
linewidth(1)
polygonA([psurf(t, q) for (t,q) in RF])
polygonA([psurf(t, q) for (t,q) in LF])
setrgbcolor('red')
polygonA([psurf(t, 0) for t in xx])
polygonA( map( proj, [[0,0,0], [1,0,0], [1, 0, f(1)]] ) )

closeOutputFile()


