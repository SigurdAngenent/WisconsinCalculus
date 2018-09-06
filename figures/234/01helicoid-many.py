from grapher3d import *

def helix(t): # 
    return ( cos(t) , sin(t) , t/(2*pi) )
###  set projection matrix     
setProjection(rotatey(pi/5, theProjection()))
setProjection(rotatez(pi/6, theProjection()))

# the triple helicoid
setViewBox(-2, -1, 2, 4) # 
openOutputFile("01helicoid-many", 200)

## The axes 
line3d([0,-1.4,0], [0,1.4,0])
line3d([-1.4,0,0], [1.4,0,0])
line3d([0,0,-1], [0,0,3.5])
### compute the helix 
nturns = 3 
he = [helix(0.02*pi*n) for n in range(nturns*100+1)]

linewidth(0.25) # 
setrgbcolor('skyblue4')
polygonA([pr(a) for a in he])
linewidth(0.25)
setrgbcolor('skyblue')
for a in he: # 
    line3d([0.0,0.0,a[2]], a)
# 
annotate( pr([1.4,0,0]) , (-2,0) , makeboxr(r"$x$") )
annotate( pr([0,1.4,0]) , (0,4) , makeboxr(r"$y$") )
closeOutputFile()


# one branch of the helicoid # 
setViewBox(-2, -1, 2, 4)
openOutputFile("01helicoid-one", 200)

## The axes 
line3d([0,-1.4,0], [0,1.4,0])
line3d([-1.4,0,0], [1.4,0,0])
line3d([0,0,-1], [0,0,3.5])
### compute the helix 
nturns = 1 
he = [helix(0.02*pi*n) for n in range(nturns*100+1)]

linewidth(0.25) # 
setrgbcolor('skyblue4')
polygonA([pr(a) for a in he])
linewidth(0.25)
setrgbcolor('skyblue')
for a in he: # 
    line3d([0.0,0.0,a[2]], a)
# 
annotate( pr([1.4,0,0]) , (-2,0) , makeboxr(r"$x$") )
annotate( pr([0,1.4,0]) , (0,4) , makeboxr(r"$y$") )
closeOutputFile()


