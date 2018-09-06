from math import *
from numpy import *
from grapher import *

def  rotatex(angle,pro): #{{{1
    c, s = cos(angle), sin(angle)
    return matrix([[1,0,0], [0,c, -s], [0, s, c]])*pro
def  rotatey(angle,pro): #{{{1
    c, s = cos(angle), sin(angle)
    return matrix([[c, 0, -s], [0,1,0], [s, 0, c]])*pro
def  rotatez(angle,pro): #{{{1
    c, s = cos(angle), sin(angle)
    return matrix([[c,-s,0], [s, c, 0], [0,0,1]]) * pro
def  pr(q): #{{{1
    """ Multiply the row matrix q with PMAT and return as list"""
    global PMAT
    qq = q*PMAT
    return [qq[0,0], qq[0,1]]

def  line3d(P,Q): #{{{1
    line(pr(matrix(P)), pr(matrix(Q)))
def  shadowlines3d(segmentlist,widths=[1,0.25]): #{{{1
    setrgbcolor('white')
    linewidth(widths[0])
    for seg in segmentlist:
        line3d(seg[0],seg[1])
    setrgbcolor('black')
    linewidth(widths[1])
    for seg in segmentlist:
        line3d(seg[0],seg[1])

PMAT = matrix( [[0,0], [1,0], [0,1]] )
PMAT = rotatey(pi/10, PMAT)
PMAT = rotatez(-pi/3, PMAT)
print( PMAT )

def  f(x,y): return sqrt(x*y) #{{{1

s1 = [mat([1, t, f(1,t)]) for t in linspace(0,3,101)]
s2 = [mat([t, 1, f(t,1)]) for t in linspace(0,3,101)]
s3 = [mat([3, t, f(3,t)]) for t in linspace(1,3,51)]
s4 = [mat([t, 3, f(t,3)]) for t in linspace(1,3,51)]

setViewBox(-1,-2,5,4) #{{{1
openOutputFile("03two-tangents", 300)

# The x and y axes.  z-axis comes later because it covers {{{1
# part of the drawing.
linewidth(2)
line3d([-1,0,0], [4,0,0])
line3d([0,-1,0], [0,3,0])
annotate(pr([4,0,0]), [0,2], makeboxc("$x$"))
annotate(pr([0,3,0]), [2,-2], makeboxl("$y$"))
annotate(pr([0,0,2]), [4,-2], makeboxl("$z$"))
annotate(pr([1,1,0]), [0, -10], makeboxc("$(a,b)$"))

# The two lines x=1 and y=1 in the xy plane {{{1
linewidth(0.5)
line3d([1,-1,0], [1, 3, 0])
line3d([-1,1,0], [3, 1, 0])

#the graph of f {{{1
linewidth(1)
for s in (s1,s2, s3, s4):
    polygonA([pr(P) for P in s])
linewidth(0.3)
for u in linspace(1, 3, 9, endpoint=False):
    s3 = [mat([u, t, f(u,t)]) for t in linspace(1,3,51)]
    s4 = [mat([t, u, f(t,u)]) for t in linspace(1,3,51)]
    polygonA([pr(P) for P in s3])
    polygonA([pr(P) for P in s4])


shadowlines3d([[[1,1,0], [1,1,1]]])
# The two tangent lines {{{1
linewidth(2)
shadowlines3d([[[1, -1, 0], [1, 3, 2]],
               [[-1, 1, 0], [3, 1, 2]]], [3,2])
shadowlines3d([[[0,0,-1], [0,0,2]]], [3, 2])

closeOutputFile()


