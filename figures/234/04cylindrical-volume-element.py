from grapher3d import *
draft=0
###  set projection matrix     {{{1

setProjection(rotatey(pi/10, theProjection ()))
setProjection(rotatez(-pi/12, theProjection ()))

setViewBox(-0.5, -0.7, 1.25, 1.7) # {{{1
openOutputFile("04cylindrical-volume-element",150)

#the axes {{{1
if draft: setrgbcolor ('green')
line3d ([-0.5,0,0], [2,0,0])
if draft: setrgbcolor ('red')
line3d([0,-0.5,0], [0,1.3,0])
if draft: setrgbcolor ('blue')
line3d([0,0,0], [0,0,1.7])

th=pi/6 ## Set parameters {{{1
dth=pi/8
cth = cos(th)
sth = sin(th)
cth2= cos(th+dth)
sth2= sin(th+dth)

#the basic arc {{{1
N=10
boog = [(cos(th+j*dth/N), sin(th+j*dth/N)) for j in range(N+1)]

polygonA([pr([p[0],p[1],0]) for p in boog])
polygonA([pr([0.8*p[0],0.8*p[1],0]) for p in boog])
line3d([0,0,0], [cth,sth,0])
line3d([0,0,0], [cth2,sth2,0])
polygonA([pr([0.6*cos(j*th/30), 0.6*sin(j*th/30), 0]) 
    for j in range(31)])

linewidth(0.6) # The box {{{1
polygonA([pr([p[0],p[1],1.3]) for p in boog])
polygonA([pr([0.8*p[0],0.8*p[1],1.3]) for p in boog])

line3d([0.8*cth,0.8*sth,1.3], [cth,sth,1.3])
line3d([0.8*cth2,0.8*sth2,1.3], [cth2,sth2,1.3])
line3d([cth, sth, 1],[cth, sth, 1.3])
line3d([0.8*cth, 0.8*sth, 1],[0.8*cth, 0.8*sth, 1.3])
linewidth(1.5)
line3d([cth2, sth2, 1], [cth2, sth2, 1.3])
line3d([0.8*cth,0.8*sth,1], [cth,sth,1])
polygonA([pr([p[0],p[1],1]) for p in boog])
linewidth(0.3)
for j in range(15):
    r=0.8+(j+1)*0.2/16
    line3d([r*cth, r*sth, 1],[r*cth, r*sth, 1.3])
    h=1+(j+1)*0.3/16
    polygonA([pr([p[0],p[1],h]) for p in boog])



setdash("[2 2] 0") # hidden lines of box {{{1
polygonA([pr([0.8*p[0],0.8*p[1],1]) for p in boog])
line3d([0.8*cth2, 0.8*sth2, 1],[0.8*cth2, 0.8*sth2, 1.3])
line3d([0.8*cth2,0.8*sth2,1], [cth2,sth2,1])
setdash("[1] 0") # Connecting lines {{{1
linewidth(0.4)
line3d([0,0,1], [cth,sth,1])
line3d([0,0,1], [cth2,sth2,1])
line3d([0,0,1.3], [cth,sth,1.3])
line3d([0,0,1.3], [cth2,sth2,1.3])
line3d([cth,sth,0], [cth,sth,1])
line3d([0.8*cth,0.8*sth,0], [0.8*cth,0.8*sth,1])
line3d([cth2,sth2,0], [cth2,sth2,1])
line3d([0.8*cth2,0.8*sth2,0], [0.8*cth2,0.8*sth2,1])
polygonA([pr([0.3*p[0],0.3*p[1],1]) for p in boog]) 
# Annotations {{{1
annotate(pr([2,0,0]), [1,1], makeboxl("$x$"))
annotate(pr([0,1.3,0]), [2,-5], makeboxl("$y$"))
annotate(pr([0,0,1.7]), [2,-10], makeboxl("$z$"))
annotate(pr([0.9*cth, 0.9*sth, 1]), [0,-8], makeboxc("$dr$"))
annotate(pr([0.6*cth, 0.6*sth, 1]), [0,-8], makeboxc("$r$"))
annotate(pr([cos(th+dth/2), sin(th+dth/2), 1]), [1,-8],
        makeboxc("$rd\\theta$"))
annotate(pr([cth2, sth2, 1.15]), [2,-4], makeboxl("$dz$"))
annotate(pr([0.6*cos(th/2), 0.6*sin(th/2),0]), [0,-7],
        makeboxl("$\\theta$"))
annotate(pr([0.3*cos(th+dth/2), 0.3*sin(th+dth/2),1]), [0,5],
        makeboxl("$d\\theta$"))
#annotate(pr([]), [], makeboxl("$$"))
closeOutputFile()


