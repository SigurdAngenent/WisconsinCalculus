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

# Set the projection matrix {{{1
PMAT = matrix( [[0,0], [1,0], [0,1]] )
PMAT = rotatey(pi/6, PMAT)
PMAT = rotatez(-pi/6, PMAT)
print( PMAT )


setViewBox(-2,-3,2,2) #{{{1
openOutputFile("03example-2nd-deriv-test-wires", 300)



#the graph of f, spoke by spoke {{{1
linewidth(1)
radii = [i/50.0 for i in range(51)]
thmin =-0.8*pi
thmax = 0.5*pi
def drawspoke(th, width=1): #{{{2
    global radii
    cth = cos(th)
    sth = sin(th)
    height = 2*sin(2*th) - 1
    spoke = [array([r*cth, r*sth, height*r*r]) for r in radii]
    #first the halo
    linewidth(2*width)
    setrgbcolor('white')
    polygonA([pr(P) for P in spoke])
    #then the wire
    linewidth(width)
    setrgbcolor('black')
    polygonA([pr(P) for P in spoke])
for th in linspace(thmin,-pi/4,26):  # draw spoke at angle th {{{2
    drawspoke(th)#, width=0.5)
for th in linspace(thmax, -pi/4, 36):
    drawspoke(th)#, width=0.5)

drawspoke(0, width=2)
drawspoke(-pi/2, width=2)
drawspoke(pi/4, width=2)
drawspoke(-3*pi/4, width=2)

#  draw the rim of the graph {{{1
angles=linspace(thmin, thmax, 101)
rim = [(cos(th), sin(th), 2*sin(2*th)-1) for th in angles]
polygonA([pr(P) for P in rim])
# The x,y  and z axes.  {{{1
linewidth(2)
line3d([-1,0,0], [2,0,0])
line3d([0,-1,0], [0,0.5,0])
line3d([0,0,0], [0,0,1])

closeOutputFile()  # Done {{{1


