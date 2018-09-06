# Time-stamp: <2012-08-02 09:10:31 angenent>
from grapher import *
from math import *
################################################################################

Pmat=[[0.8, -0.2],
      [0.4, 0.2],
      [0, 1]]
def proj(X):  #linear projection of R^3 onto R^2 
    global Pmat
    x=sum([Pmat[i][0]*X[i] for i in range(3)])
    y=sum([Pmat[i][1]*X[i] for i in range(3)])
    return [x, y]

def drawslice(h, linetozaxis='YES'):
    global T, base
    q=1-h
    slice=[ [q*P[0]+(1-q)*T[0],
             q*P[1]+(1-q)*T[1],
             q*P[2]+(1-q)*T[2]] for P in base]
    polygonA(map(proj, slice[:3]))
    setdash("[3] 0")
    setrgbcolor('black')
    linewidth(0.5)
    if(linetozaxis!='NO'):
        polygonA(map(proj, slice[-3:]))
        line(proj(slice[0]),  proj( [0,0,slice[0][2]] )  )
    setdash("[] 0")
    linewidth(1)

################################################################################

setViewBox(0, -0.5, 1.5, 1.5)
openOutputFile("09pyramid",180)
base=[[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,0]]
T=[0.2, 0.3, 1]


polygonA(map(proj, base[:3]))
for P in base[:3]:
    line(proj(T), proj(P))
    line(proj(T), proj(P))
    line(proj(T), proj(P))
setdash("[3] 0")
polygonA(map(proj, base[-3:]))
line(proj(T), proj(base[3]))
line(proj(T), proj([0,0,1]))
setdash("[] 0")

drawslice(0.6)
drawslice(0.65)
linewidth(0.25)
for h in (0.61, 0.62, 0.63, 0.64):
    drawslice(h, linetozaxis='NO')
linewidth(0.5)
line(proj([0, 0, 0]), proj([0,0,1.3]))
annotate(proj([0.5, 0, 0]), [0, -9], "$1$")
annotate(proj([1.0, 0.5, 0]), [5, -5], "$1$")

#labels on the z-axis
annotate(proj([0,0,0]), [-6, -4], makeboxr("$0$"))
annotate(proj([0,0,0.6]), [-6, -4], makeboxr("$x$"))
annotate(proj([0,0,0.65]), [-3, 0], makeboxr("$x+\Delta x$"))
annotate(proj([0,0,1]), [-6, -4], makeboxr("$1$"))

closeOutputFile()


