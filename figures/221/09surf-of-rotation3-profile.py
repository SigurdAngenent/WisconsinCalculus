#Time-stamp: <Wednesday August 01 2012 16:24:26>

from grapher import *
from math import *
################################################################################
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
################################################################################
def jac(X, u, v):
    eps = 0.000001
    A = map(lambda p,q: (p-q)/eps, X(u+eps/2, v), X(u-eps/2, v))
    B = map(lambda p,q: (p-q)/eps, X(u, v+eps/2), X(u, v-eps/2))
    return A[0]*B[1]-A[1]*B[0]
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
def fold(t, zmin, zmax):
  return bisect(lambda z:jac(psurf, t, z), zmin, zmax)
def rad(x): return 1.2*exp(-x/2.0)#2/(2.0+x)
def surf(t, z):
    r=rad(t)
    return [t, r*cos(z), r*sin(z)]
def psurf(t,z): return proj(surf(t,z))
def surfin(t, z):
    r=0.5*rad(t)
    return [t, r*cos(z), r*sin(z)]
def psurfin(t,z): return proj(surfin(t,z))
def drawdiscF(t, fillcolor='lightGray'):
    ppout = [psurf(t, 2*i*pi/100) for i in range(101)]
    ppin = [psurfin(t, 2*i*pi/100) for i in range(101)]
    ppin.reverse()
    polygonPath(ppout)
    polygonF(ppin, fillcolor)
    polygonC(ppout)
    polygonC(ppin)
def swing(x, r, anglestart, angleswing):
    th = [k*angleswing/100+anglestart for k in range(101)]
    pp = [ [x, r*cos(t), r*sin(t)] for t in th]
    polygonA(map(proj, pp))
    #now the arrow
    angleend = anglestart + angleswing
    ar = [[x, r*cos(angleend), r*sin(angleend)]]
    ar.append([x, (r+0.1)*cos(angleend-pi/9), (r+0.1)*sin(angleend-pi/9) ])
    ar.append([x, (r)*cos(angleend-pi/24), (r)*sin(angleend-pi/24) ])
    ar.append([x, (r-0.1)*cos(angleend-pi/9), (r-0.1)*sin(angleend-pi/9) ])
    ar = map(proj,ar)
    polygonF(ar)
    polygonA(ar)
#############################################################################

# decide on a projection
make_Pmat([2,-2,1])

setViewBox(-1.0, -1.5, 4.0, 1.5)
openOutputFile("09surf-of-rotation3-profile",175)
#x-axis
line(proj([-1,0,0]), proj([4,0,0]))

#the graph of f
tt= [0.1*i for i in range(31)]
region = [psurf(t, pi/2) for t in tt]
region.reverse()
region.extend( [psurfin(t, pi/2) for t in tt] )
linewidth(2)
polygonC(region)
#region.extend([proj([3,0,0]), proj([0,0,0])])
polygonF(region, 'lightGray')
#Arrows
linewidth(1)
line(proj( [0,0,0] ), proj( [0,0,1.3] ))
line(proj( [3,0,0] ), psurf(3.0, pi/2) )
ar = map(proj,
         [[4.05,0,0], [3.8, 0.1, 0], [3.9, 0, 0],
          [3.8, -0.1, 0], [4.05,0,0]])
polygonF(ar, fillcolor='black')
polygonC(ar)
arrow( proj([1.0, 0, 0]),  psurfin(1.0, pi/2), 3, 1, -2)
# show the direction of rotation :
linewidth(2)
swing(0.7, 0.75*rad(0.7), pi/2, 1.25*pi)
#Annotations
annotate(psurf(1.0, pi/2), [3, 0], makeboxl("$r=r_{\\rm out}$") )
annotate(psurfin(1.0, pi/2), [-1, -5], makeboxr("$r_{\\rm in}$") )
annotate(proj([3.5, 0, 0]), [2, 2], "$x$-axis")
annotate(proj([0, 0, 1.2]), [-2, 0], makeboxr("$r$"))


closeOutputFile()


