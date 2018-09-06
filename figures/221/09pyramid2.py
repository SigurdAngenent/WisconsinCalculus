# Time-stamp: Aug  2 11:18 09pyramid2.py
from grapher import *
from math import *
# Set Pmat
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
def drawslice(h, fillcolor):
      global T, base
      q=1-h
      slice=[ [q*P[i]+(1-q)*T[i] for i in range(3)] for P in base]
      polygonF(map(proj, slice), fillcolor)
      polygonA(map(proj, slice[:3]))
      linewidth(0.25)
      polygonA(map(proj, slice[-3:]))
      #setdash("[3] 0")
      line(proj(slice[0]),  proj( [0,0,slice[0][2]] )  )
      #setdash("[] 0")
      linewidth(1)
#  Main 
make_Pmat([1,-2,1])
print Pmat

setViewBox(-0.2, -0.5, 1.5, 1.2)
openOutputFile("09pyramid2",180)
base=[[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,0]]
T=[0.5, 0.5, 1]
#Shadow of pyramid
wall = [[0,1.4,0], [0,1.4,1.1], [0, -0.6, 1.1], [0, -0.6, 0]]
wall = map(proj, wall)
polygonF(wall, [240,240,240])
sh = [[0,0,0], [0,1,0], [0,0.5,1]]
sh = map(proj, sh)
polygonF(sh, [220,220,220])
sh = [[0,0.285, 0.57], [0, 0.715, 0.57], [0, 0.7,0.6], [0, 0.3, 0.6]]
sh = map(proj, sh)
polygonF(sh, [96,96,96])
#Base and back edges
polygonA(map(proj, base[:3]))
setdash("[3] 0")
polygonA(map(proj, base[-3:]))
line(proj(T), proj(base[3]))
line(proj(T), proj([0,0,1]))
setdash("[] 0")
#slices
drawslice(0.57, [96,96,96])
drawslice(0.6, "lightGray")
#front edges and x-axis:
for P in base[:3]:
      line(proj(T), proj(P))
      line(proj(T), proj(P))
      line(proj(T), proj(P))
line(proj([0, 0, 0]), proj([0,0,1.25]))
ar = [[0, 0,    1.3], #arrow on the vertical axis
      [0, 0.05, 1.2],
      [0, 0,    1.23],
      [0,-0.05, 1.2]]
ar = map(proj, ar)
polygonF(ar, 'black')
polygonC(ar)
# arrows to the top and bottom slices
arrow(proj([0.5, 1, 0.9]), proj([0.7, 0.5, 0.64]), 7, 2)
annotate(proj([0.5, 1, 1]), [2,-2], makeboxc("side\,$=1-x_k$") )
arrow(proj([0.9, 0.85, 0.4]), proj([0.73, 0.5, 0.57]), 7, 2)
annotate(proj([0.9, 0.9, 0.35]), [0,0], makeboxl("side\,$=1-x_{k-1}$") )
annotate(proj([0.5, 0, 0]), [0, -9], "$1$")
annotate(proj([1.0, 0.5, 0]), [5, -5], "$1$")
#labels on the z-axis
annotate(proj([0,0,0]), [-6, -4], makeboxr("$0$"))
annotate(proj([0,0,0.6]), [1, 4], makeboxl("$x_k$"))
annotate(proj([0,0,0.57]), [1, -6], makeboxl("$x_{k-1}$"))
annotate(proj([0,0,1]), [-6, -4], makeboxr("$1$"))
annotate(proj([0,0,1]), [-6, -4], makeboxr("$1$"))
annotate(proj([0,0.1,1.2]), [1, 4], makeboxl("$x$"))



closeOutputFile()


