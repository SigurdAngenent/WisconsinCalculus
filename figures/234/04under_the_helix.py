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
def cubic(t): # {{{1
    return (t, t*t, t*t*t)
def helix(t): # {{{1
    return (cos(t), sin(t), t/2)
###  set projection matrix     {{{1
PMAT = [[0,0], [1,0], [0,1]]
PMAT = rotatey(pi/6, PMAT)
PMAT = rotatez(pi/6, PMAT)
print( PMAT )


setViewBox(-0.75, -1, 1.25, 1) # {{{1
openOutputFile("04under-the-helix", 240)

linewidth(0.5) #the axes {{{1
line3d([0,-0.4,0], [0,0.0,0])
line3d([0,1.4,0], [0,1.0,0])
line3d([1,0,0], [1.4,0,0])
line3d([0,0,-0.7], [0,0,1.0])
setdash("[2] 0")
line3d([0,0.0,0], [0,1.0,0])
line3d([-1,0,0], [0,0,0])
setdash("[] 0")
### compute the helix {{{1
nturns = 0.25  ## we'll draw one quarter term of the helix
he = [helix(nturns*0.02*pi*(n)) for n in range(101)]
print( he[0] )

linewidth(1) # {{{1 draw the helix
polygonA([pr(a) for a in he])
polygonA([pr([a[0],a[1],0.0]) for a in he])
line3d([0,1,0], [0,1,pi/4])
line3d([0,0,pi/4], [0,1,pi/4])
linewidth(0.25)
b=he[0]
for a in he: # draw the helicoid and vertical wall {{{1
    line(pr([0.0,0.0,a[2]]), pr([a[0],a[1],a[2]]))
    line(pr([a[0],a[1],0.0]), pr([a[0],a[1],a[2]]))
### The surrounding cylinder {{{1
line3d([1,0,0], [1,0,pi/4])
line3d([0,0,pi/4], [1,0,pi/4])
polygonA([pr([a[0],a[1],pi/4]) for a in he])
### Annotations {{{1
annotate(pr([1.4,0,0]),  [0,-8],  "$x$")
annotate(pr([0,1.4,0]),  [-8,-8], "$y$")
annotate(pr([0,0,1.0]),  [3,-4],   makeboxl("$z$"))
annotate(pr([0,0,pi/4]), [-7,0],  makeboxr("$\\pi/4$"))
closeOutputFile()


