from grapher3d import *

def cubic(t): # {{{1
    return (t, t*t, t*t*t)

def helix(t): # {{{1
    return (cos(t), sin(t), t/4)

## SET THE PROJECTION MATRIX     {{{1
setProjection( [[0,0], [1,0], [0,1]] )
setProjection( rotatey( pi/5, theProjection()) )
setProjection( rotatez( pi/3, theProjection()) )


setViewBox(-1.3, -1, 1.5, 2.3) # {{{1
openOutputFile("05helix", 150)

## THE AXES {{{1
linewidth(0.5) 
line3d([0,-1.4,0], [0,1.4,0])
line3d([-1.4,0,0], [1.4,0,0])
line3d([0,0,0], [0,0,2.0])
## COMPUTE THE HELIX {{{1
nturns = 1.00  ## we'll draw a whole turn of the helix
he = [helix(nturns*0.02*pi*(n)) for n in range(101)]
print( he[0] )
## DRAW THE SCAFFOLDING{{{1
p = he[35]
scaf = [ pr([1,0,0]), pr([0,0,0]), pr([p[0],p[1],0]), pr(p) ]
setrgbcolor("sienna")
linewidth(2) 
polygonA(scaf)
## DRAW THE HELIX{{{1
setrgbcolor("deepskyblue")

polygonA([pr(a) for a in he])
## SURROUNDING CYLINDER {{{1
setrgbcolor("black")
linewidth(0.25)
polygonA([pr([a[0],a[1],0.0]) for a in he])
polygonA([pr([a[0],a[1],pi/2]) for a in he])

for zeta in (5*pi/6, -pi/6):
    cz, sz = cos(zeta), sin(zeta)
    line3d([cz, sz, 0], [cz, sz, pi/2]) 

line3d([1,0,pi/2], [0, 0, pi/2])
## ANNOTATIONS {{{1
annotate(pr([1.4,0,0]),  [-2,-2],  makeboxr("$x$"))
annotate(pr([0,1.4,0]),  [2, -2], "$y$")
annotate(pr([0,0,2.0]),  [0,2],   makeboxc("$z$"))
annotate(pr([0,0, pi/2]),  [1,-2],   makeboxl(r"$\tfrac{\pi}{2}$"))
annotate(pr([1,0,0]),  [1,4],   makeboxc("$1$"))
annotate(pr([0,1,0]),  [1,3],   makeboxc("$1$"))
prhe35 = pr( he[35] )
prhe35shifted = [prhe35[0]+30, prhe35[1]]
arrow(prhe35shifted, prhe35, 7,2)
annotate(prhe35, [30,0], makeboxl(r"$(R\cos\theta, R\sin\theta, a\theta)$") )
closeOutputFile()


