from math import *
from grapher import *

def rotatex(angle,pro):
    c, s = cos(angle), sin(angle)
    ro = [[1,0,0], [0,c, -s], [0, s, c]]
    qro = [ [r[0]*pro[0][0]+r[1]*pro[1][0]+r[2]*pro[2][0],
             r[0]*pro[0][1]+r[1]*pro[1][1]+r[2]*pro[2][1]]
            for r in ro]
    return qro
def rotatey(angle,pro):
    c, s = cos(angle), sin(angle)
    ro = [[c, 0, -s], [0,1,0], [s, 0, c]]
    qro = [ [r[0]*pro[0][0]+r[1]*pro[1][0]+r[2]*pro[2][0],
             r[0]*pro[0][1]+r[1]*pro[1][1]+r[2]*pro[2][1]]
            for r in ro]
    return qro
def rotatez(angle,pro):
    c, s = cos(angle), sin(angle)
    ro = [[c,-s,0], [s, c, 0], [0,0,1]]
    qro = [ [r[0]*pro[0][0]+r[1]*pro[1][0]+r[2]*pro[2][0],
             r[0]*pro[0][1]+r[1]*pro[1][1]+r[2]*pro[2][1]]
            for r in ro]
    return qro
def pr(q):
    global PMAT
    return [q[0]*PMAT[0][0] + q[1]*PMAT[1][0] + q[2]*PMAT[2][0],
        q[0]*PMAT[0][1] + q[1]*PMAT[1][1] + q[2]*PMAT[2][1]]

PMAT = [[0,0], [1,0], [0,1]]
PMAT = rotatey(pi/6, PMAT)
PMAT = rotatez(pi/6, PMAT)
print( PMAT )


setViewBox(-2, -2, 2, 2)
openOutputFile("02localmax", 400)

linewidth(0.5)
line(pr([0,-1.4,0]), pr([0,1.4,0]))
line(pr([-1.4,0,0]), pr([1.4,0,0]))
line(pr([0,0,-1.4]), pr([0,0,2.2]))

linewidth(2)
he = [helix(0.02*pi*(n)) for n in range(101)]
polygonA([pr(a) for a in he])
linewidth(0.25)
b=he[0]
for a in he:
    setrgbcolor('white')
    linewidth(1)
    line(pr([0.02*a[0],0.02*a[1],a[2]]), pr([0.95*a[0],0.95*a[1],a[2]]))
    setrgbcolor('black')
    linewidth(0.25)
    line(pr([0,0,a[2]]), pr(a))
closeOutputFile()


