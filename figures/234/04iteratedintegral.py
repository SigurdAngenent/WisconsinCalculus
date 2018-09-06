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


#  Set rotation matrix {{{1
PMAT = matrix( [[0,0], [1,0], [0,1]] )
PMAT = rotatey(pi/10, PMAT)
PMAT = rotatez(pi/3, PMAT)
print( PMAT )

def fun(x, y): return exp(-1+3*x+y-x*x-y*y)
def drawslice(y, dy): #{{{1
    xx=[1+0.05*k for k in range(41)]
    back=[[1,y,0]]
    back.extend([[x, y, fun(x, y)] for x in xx])
    back.extend([[3,y,0],[1,y,0]])
    front = [[p[0], p[1]+dy, p[2]] for p in back]
    polygonA([pr(p) for p in back])
    polygonF([pr(p) for p in back],'white')
    for p in back:
        line3d(p, [p[0], p[1]+dy, p[2]])
    polygonF([pr(p) for p in front],"white")


setViewBox(-4,-2,2,4) #{{{1
openOutputFile("04iteratedintegral", 300)

# The axes. {{{2
linewidth(2)
line3d([-1,0,0], [4,0,0])
line3d([0,-1,0], [0,3,0])
line3d([0,0,0], [0,0,4])


linewidth(0.4)
y=0.5
dy=0.05
while y<1.999:
    drawslice(y, dy)
    y+=dy
closeOutputFile()

