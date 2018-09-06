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

def fun(x, y): return x*x+y*y #{{{1

def xstripe(x): #{{{1
    dy = 0.5/50
    pol = [[x, k*dy, fun(x, k*dy)] for k in range(51)]
    pol = [pr(matrix(pt)) for pt in pol]
    polygonA(pol)

def ystripe(y): #{{{1
    dx = 1.0/50
    pol = [[k*dx, y, fun(k*dx, y)] for k in range(51)]
    pol = [pr(matrix(pt)) for pt in pol]
    polygonA(pol)

setViewBox(-0.5, -0.2, 1.3, 1.8) #{{{1
openOutputFile("04Doubleint-example1", 200)


for x in (0.0, 1.0):
    xstripe(x)
for y in (0.0, 0.5):
    ystripe(y)

linewidth(0.4)
xlist = [k*0.05 for k in range(1,20)]
for t in xlist:
    xstripe(t)
    ystripe(t/2)

for k in range(41):
    t=0.025*k
    line3d([0,t/2,0], [0, t/2, fun(0,t/2)])
    line3d([t,0,0], [t, 0, fun(t,0)])
linewidth(0.2)
setdash("[2 2] 0")
#line3d([0,0,0], [0,0.5,0])
line3d([-0.2,0.5,0], [1,0.5,0])
line3d([1,0.5,0], [1,-0.2,0])
line3d([1,0,0], [0,0,0])
line3d([1,0.5,0], [1, 0.5, fun(1,0.5)])

# The axes. {{{1
setdash("[] 0")
linewidth(1)
line3d([-0.3,0,0], [1.2,0,0])
line3d([0,-0.3,0], [0,1.2,0])
shadowline3d([0,0,0.05], [0,0,2], [2.5, 1])
line3d([0,0,-0.2], [0,0,2])
# The surrounding block {{{1
linewidth(0.5)
top = fun(1, 0.5)
line3d([1,0,fun(1,0)], [1,0, top])
line3d([1,0.5, top], [1,0, top])
line3d([1,0.5, top], [0,0.5, top])
line3d([0,0.5, fun(0,0.5)], [0,0.5, top])
line3d([0,0, top], [0,0.5, top])
line3d([0,0, top], [1,0, top])
# Annotation {{{1
PStext (pr([1,0,0]), [-5,-12], "a", 'Palatino-Italic', 12)
PStext (pr([0,0.5,0]), [-10,0], "b", 'Palatino-Italic', 12)
PStext (pr([1.2,0,0]), [0, 3], "x", 'Palatino-Italic', 12)
PStext (pr([0,1.2,0]), [3, 0], "y", 'Palatino-Italic', 12)
PStext (pr([0,0,2]), [3, 0], "z", 'Palatino-Italic', 12)



closeOutputFile()
