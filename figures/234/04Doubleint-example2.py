from math import *
from numpy import *
from grapher import *

def rotatex(angle,pro): #{{{1
    c, s = cos(angle), sin(angle)
    return matrix([[1,0,0], [0,c, -s], [0, s, c]])*pro
def rotatey(angle,pro): #{{{1
    c, s = cos(angle), sin(angle)
    return matrix([[c, 0, -s], [0,1,0], [s, 0, c]])*pro
def rotatez(angle,pro): #{{{1
    c, s = cos(angle), sin(angle)
    return matrix([[c,-s,0], [s, c, 0], [0,0,1]]) * pro
def pr(q): #{{{1
    """ Multiply the row matrix q with PMAT and return as list"""
    global PMAT
    qq = q*PMAT
    return [qq[0,0], qq[0,1]]

def line3d(P,Q): #{{{1
    line(pr(matrix(P)), pr(matrix(Q)))
def shadowline3d(A, B,widths=[1,0.25]): #{{{1
    setrgbcolor('white')
    linewidth(widths[0])
    line3d(A,B)
    setrgbcolor('black')
    linewidth(widths[1])
    line3d(A,B)


#  Set rotation matrix {{{1
PMAT = matrix( [[0,0], [1,0], [0,1]] )
PMAT = rotatey(pi/5, PMAT)
PMAT = rotatez(-1.9, PMAT)
print( PMAT )

def fun(x, y): return x+y #{{{1
def xbot(y): return 1-sqrt(y)
def ybot(x): return (x-1)*(x-1)

def xstripe(x): #{{{1
    yb=ybot(x)
    dy = (1.0-yb)/50
    pol = [[x, yb+k*dy, fun(x, yb+k*dy)] for k in range(51)]
    pol = [pr(matrix(pt)) for pt in pol]
    polygonA(pol)

def ystripe(y): #{{{1
    xb=xbot(y)
    dx = (1.0-xb)/50
    pol = [[xb+k*dx, y, fun(xb+k*dx, y)] for k in range(51)]
    pol = [pr(matrix(pt)) for pt in pol]
    polygonA(pol)

setViewBox(-0.5,-0.2,1.3,2.5) #{{{1
openOutputFile("04Doubleint-example2", 192)

xstripe(1.0)
ystripe(1.0)
tlist=[0.01*k for k in range(101)]
edge = [[t, ybot(t), fun(t, ybot(t))] for t in tlist]
polygonA ([pr (matrix(P)) for P in edge])
polygonA ([pr (matrix([P[0],P[1],0])) for P in edge])
line3d([1,0,0], [1, 0, fun(1,0)])
line3d([0,1,0], [0, 1, fun(0,1)])

linewidth(0.4)
tlist = [k*0.05 for k in range(1,20)]
for t in tlist:
    xstripe(t)
    ystripe(t)

for k in range(81):
    t=0.0125*k
    xb, yb = t, ybot(t)
    line3d([xb,yb,0], [xb, yb, fun(xb, yb)])

# The surrounding box {{{1
top=fun(1,1)
linewidth(0.4)
line3d([1,0,fun(1,0)], [1,0,top])
line3d([0,1,fun(0,1)], [0,1,top])
line3d([1,0,top], [1,1,top])
line3d([0,1,top], [1,1,top])
polygonA ([pr (matrix([P[0],P[1],top])) for P in edge])
linewidth(0.2)
setdash("[2 2] 0")
line3d([0,0,0], [0,1,0])
line3d([0,1,0], [1,1,0])
line3d([1,1,0], [1,0,0])
line3d([1,0,0], [0,0,0])
line3d([1,1,0], [1, 1, fun(1,1)])
# The axes. {{{1
setdash("[] 0")
linewidth(1)
line3d([-0.3,0,0], [1.2,0,0])
line3d([0,-0.3,0], [0,1.2,0])
shadowline3d([0,0,0.05], [0,0,3.0], [4, 1])
line3d([0,0,-0.2], [0,0,3.0])
# Annotations  {{{1
PStext(pr([1.2,0,0]), [2,-3], "x", "Palatino-Italic", 10)
PStext(pr([0,1.2,0]), [-5,-3], "y", "Palatino-Italic", 10)
PStext(pr([0,0,3.0]), [2,-7], "z", "Palatino-Italic", 10)
closeOutputFile()

#  Draw the domain {{{1
setViewBox (-0.5, -0.5, 1.5, 1.5)
openOutputFile ("04Doubleint-example2-domain", 96)
axes([7,7])
po = [0.01*k for k in range(101)]
po = [[1-x, x*x] for x in po]
po.extend([[1.0,1.0], [1.0, 0.0]])
polygonF (po, [255,128,0])
PStext([1.4,0], [0,3], "x", "Palatino-Italic", 10)
PStext([0,1.5], [3,-3], "y", "Palatino-Italic", 10)
PStext([1,0], [-2, -8], "1", "Palatino-Italic", 10)
PStext([0,1], [-6, -3], "1", "Palatino-Italic", 10)
PStext([0.6, 0.55], [0,0], "D", "Palatino-Italic", 10)
closeOutputFile ()

# Draw domain with partition {{{2

setViewBox (-0.5, -0.5, 1.5, 1.5)
openOutputFile ("04Doubleint-example2-partition", 96)
axes([7,7])
N, M = 12, 16
dy, dx = 1.0/N, 1.0/M

linewidth(0.4)
for k in range(N):  # Horizontal stripes  {{{
    y=k*dy
    ylist = [y+l*dy*0.1 for l in range(11)]
    edge=[(xbot(t), t) for t in ylist]
    edge.extend([[1, y+dy],[1,y],[xbot(y), y]])
    polygonA(edge)
    if 2*k==N:
        polygonF(edge, [196,0,0]) #}}}
for k in range(M):# Vertical stripes {{{
    x=k*dx
    line([x,ybot(x)], [x, 1])

PStext([1.4,0], [0,3], "x", "Palatino-Italic", 10)
PStext([0,1.5], [3,-3], "y", "Palatino-Italic", 10)
PStext([1,0], [-2, -8], "1", "Palatino-Italic", 10)
PStext([0,1], [-6, -3], "1", "Palatino-Italic", 10)
closeOutputFile ()


