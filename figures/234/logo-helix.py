from math import *
from grapher import *

def shadowline(A,B,widths=[2,0.25]):
    setrgbcolor('white')
    linewidth(widths[0])
    line([0.96*A[0]+0.04*B[0], 0.96*A[1]+0.04*B[1]],
         [0.04*A[0]+0.96*B[0], 0.04*A[1]+0.96*B[1]])
    setrgbcolor('black')
    linewidth(widths[1])
    line(A,B)
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
def helix(t): return (cos(t), sin(t), t/pi)
def evolute(t): return (cos(t)+t*sin(t), sin(t)-t*cos(t), 0)
def pr(q):
    global PMAT
    return [q[0]*PMAT[0][0] + q[1]*PMAT[1][0] + q[2]*PMAT[2][0],
        q[0]*PMAT[0][1] + q[1]*PMAT[1][1] + q[2]*PMAT[2][1]]

PMAT = [[0,0], [1,0], [0,1]]
PMAT = rotatey(pi/6, PMAT)
PMAT = rotatez(pi/6, PMAT)
print PMAT


setViewBox(-2, -2, 2, 2)
openOutputFile("logo-helix", 400)

linewidth(0.5)
D=1.4
line(pr([0,-D,0]), pr([0,D,0]))
line(pr([-D,0,0]), pr([D,0,0]))
line(pr([0,0,0]), pr([0,0,2.2]))
polygonC([pr([-D,-D,0]), 
          pr([D, -D, 0]),
          pr([D, D, 0]),
          pr([-D, D, 0])])

tValues = [0.02*pi*n for n in range(101)]
he = [(helix(t), evolute(t)) for t in tValues]
for [a,b] in he[:30]:
    shadowline(pr(a), pr(b))
linewidth(2)
polygonA([pr(a[0]) for a in he])
polygonA([pr(a[1]) for a in he[:30]])
linewidth(0.25)
b=he[0]
for segment in he:
    a=segment[0]
    shadowline(pr([0,0,a[2]]), pr(a))

closeOutputFile()


