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
def cubic(t):
    return (t, t*t, t*t*t)
def pr(q):
    global PMAT
    return [q[0]*PMAT[0][0] + q[1]*PMAT[1][0] + q[2]*PMAT[2][0],
        q[0]*PMAT[0][1] + q[1]*PMAT[1][1] + q[2]*PMAT[2][1]]

PMAT = [[0,0], [1,0], [0,-1]]
PMAT = rotatey(pi/5, PMAT)
PMAT = rotatez(pi/6, PMAT)
print( PMAT )

qbicfront = [cubic(-1+k*0.02) for k in range(51)]
qbicback = [cubic(k*0.02) for k in range(42)]

setViewBox(-2, -2, 2, 2)
openOutputFile("03osculating", 400)

linewidth(0.5)
line(pr([0,-1,0]), pr([0,1,0]))
linewidth(0.25)
for q in qbicback:
    polygonA([pr(q), pr([q[0] , q[1], 0]), pr([q[0] , 0, 0])])

for q in qbicfront:
    linewidth(0.5)
    setrgbcolor('white')
    polygonA([pr([0, q[1],q[2]]),
        pr(q),
        pr([q[0] , q[1], 0]),
        pr([q[0] , 0, 0])])
    linewidth(0.25)
    setrgbcolor('gray')
    polygonA([pr([0, q[1],q[2]]),
        pr(q),
        pr([q[0] , q[1], 0]),
        pr([q[0] , 0, 0])])
linewidth(1)
setrgbcolor('black')
polygonA([pr(q) for q in qbicback])
polygonA([pr(q) for q in qbicfront])
linewidth(0.5)
line(pr([-1,0,0]), pr([1,0,0]))
polygonA([pr([0,q[1],q[2]]) for q in qbicfront])
polygonA([pr([q[0],q[1],0]) for q in qbicfront])
polygonA([pr([q[0],q[1],0]) for q in qbicback])
linewidth(2)
setrgbcolor('white')
line(pr([0,0,-1]), pr([0,0,-0.1]))
linewidth(0.5)
setrgbcolor('black')
line(pr([0,0,-1]), pr([0,0,1]))
closeOutputFile()


