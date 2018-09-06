from grapher3d import *

def helix(t): # {{{1
    return (cos(t), sin(t), t/pi)
###  set projection matrix     {{{1
print( theProjection() )
setProjection(rotatey(pi/6, theProjection()))
setProjection(rotatez(pi/6, theProjection()))
print( theProjection() )

print( pr([1,0,0],1) )

setViewBox(-2, -4, 2, 4) # {{{1
openOutputFile("04helix", 400)

## The axes {{{1
line3d([0,-1.4,0], [0,1.4,0])
line3d([-1.4,0,0], [1.4,0,0])
line3d([0,0,-1.4], [0,0,4.2])
### compute the helix {{{1
nturns = 2  ## we'll draw 2 turns of the helix
he = [helix(nturns*0.005*pi*(n)) for n in range(401)]

linewidth(2) # {{{1 draw the helix
polygonA([pr(a) for a in he])
linewidth(0.25)
for a in he: # {{{2
    line3d([0.0,0.0,a[2]], a)
closeOutputFile()


