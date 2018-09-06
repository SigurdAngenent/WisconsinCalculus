# vim: tw=80 fdm=marker 
from math import *
from grapher import *

def shadowline(A,B,widths=[1,0.25], linecolor='black'):  #{{{1
    setrgbcolor('white')
    linewidth(widths[0])
    line(A,B)
    setrgbcolor(linecolor)
    linewidth(widths[1])
    line(A,B) 
def rotatex(angle,pro):  #{{{1
    c, s = cos(angle), sin(angle)
    ro = [[1,0,0], [0,c, -s], [0, s, c]]
    qro = [ [r[0]*pro[0][0]+r[1]*pro[1][0]+r[2]*pro[2][0],
             r[0]*pro[0][1]+r[1]*pro[1][1]+r[2]*pro[2][1]]
            for r in ro]
    return qro  
def rotatey(angle,pro):  #{{{1
    c, s = cos(angle), sin(angle)
    ro = [[c, 0, -s], [0,1,0], [s, 0, c]]
    qro = [ [r[0]*pro[0][0]+r[1]*pro[1][0]+r[2]*pro[2][0],
             r[0]*pro[0][1]+r[1]*pro[1][1]+r[2]*pro[2][1]]
            for r in ro]
    return qro  
def rotatez(angle,pro):  #{{{1
    c, s = cos(angle), sin(angle)
    ro = [[c,-s,0], [s, c, 0], [0,0,1]]
    qro = [ [r[0]*pro[0][0]+r[1]*pro[1][0]+r[2]*pro[2][0],
             r[0]*pro[0][1]+r[1]*pro[1][1]+r[2]*pro[2][1]]
            for r in ro]
    return qro  
def cubic(t):  #{{{1
    return (t, t*t, t*t*t)  
def helix(t): #{{{1
  return (cos(t), sin(t), t/pi) 
def pr(q):  #{{{1
    global PMAT
    return [q[0]*PMAT[0][0] + q[1]*PMAT[1][0] + q[2]*PMAT[2][0],
        q[0]*PMAT[0][1] + q[1]*PMAT[1][1] + q[2]*PMAT[2][1]]


PMAT = [[0,0], [1,0], [0,1]]  #{{{1
PMAT = rotatey(pi/6, PMAT)
PMAT = rotatez(pi/6, PMAT)
print( PMAT )


setViewBox(-2, -2, 2, 2) #{{{1
openOutputFile("03helix-wall", 400)
#{{{1  draw the XYZ axes
linewidth(1)
line(pr([0,-1.4,0]), pr([0,1.4,0]))
line(pr([-1.4,0,0]), pr([1.4,0,0]))
line(pr([0,0,-1]), pr([0,0,0.2]))

linewidth(2)
he = [helix(0.02*pi*(n)) for n in range(101)]   #{{{1 compute the helix
setrgbcolor('darkgreen')
polygonA([pr([a[0],a[1], 0]) for a in he])  #{{{1 draw the base circle
#{{{1  draw the vertical stiles
linewidth(0.25)
b=he[0]
setlinecap(0)
for a in he:  
    bot,top = 0.02, a[2]-0.01
    if bot<top:
        shadowline(pr([a[0],a[1],bot]), pr([a[0],a[1],top]), [1,0.25], 'limegreen')
#{{{1 draw the helix
setlinecap(1)
linewidth(2)
setrgbcolor('blue')
polygonA([pr(a) for a in he])
setlinecap(0)
shadowline(pr([0,0,0.2]), pr([0,0,2]), [2,1])
closeOutputFile()


