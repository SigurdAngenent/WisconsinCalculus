from grapher3d import *
draft=0
###  set projection matrix     {{{1

setProjection(rotatey(pi/7, theProjection ()))
setProjection(rotatez(-pi/6, theProjection ()))

def sph(rho, phi, th): #{{{1
    sphi = sin(phi)
    cphi = cos(phi)
    sth  = sin(th)
    cth  = cos(th)
    return [rho*sphi*cth, rho*sphi*sth, rho*cphi]

def prsph(rho, phi, th): #{{{1
    return pr(sph(rho, phi, th))
def cyl(r, th, z): #{{{1
    return (r*cos(th), r*sin(th), z)
def prcyl(r, th, z): #{{{1
    return pr(cyl(r, th, z))
def drawhorizarc(th0, th1, phi, rho, N=11): #{{{1
    thstep = (th1-th0)/(N-1.0)
    polygonA([prsph(rho, phi, th0+j*thstep) for j in range(N)])
def drawvertarc(th, phi0, phi1, rho, N=11): #{{{1
    phistep = (phi1-phi0)/(N-1.0)
    polygonA([prsph(rho, phi0+j*phistep, th) for j in range(N)])

## Set parameters, th, phi, rho {{{1
origin = [0,0,0]
th=pi/4  
phi=3*pi/12 
rho=1.0
r=0.8
z= 0.5

setViewBox(-0.2, -0.5, 1.25, 1.0) #  Spherical coordinates {{{1
openOutputFile("04spherical-coordinates", 120)

#the axes  (x green, y red, z blue) {{{1
if draft: linewidth(2)
if draft: setrgbcolor ('green')
line3d ([-0.5,0,0], [1,0,0])
if draft: setrgbcolor ('red')
line3d([0,-0.5,0], [0,0.7,0])
if draft: setrgbcolor ('blue')
line3d([0,0,0], [0,0,1.0])
if draft: linewidth(1)

# drawing of the coordinates {{{1
if draft==1: 
    setrgbcolor('eggplant')
A = sph(rho, phi, th)
line3d(origin, A)
linewidth(0.4)
drawvertarc(th, 0, phi, rho/3)
drawhorizarc(0,th, pi/2, rho/4)
line3d(origin, [1.5*A[0], 1.5*A[1], 0])
setdash("[3 2 0.5 2] 0")
line3d([0,0,A[2]], A)
line3d(A, [A[0],A[1],0])
line3d([A[0],0,0], [A[0],A[1],0])
line3d([0,A[1],0], [A[0],A[1],0])
setdash("[] 0")
roundPoint(pr(A))
#Annotations
annotate(prsph(rho/3, phi/2, th), [1,1], makeboxc("$\\phi$"))
annotate(prsph(rho/4, pi/2, th/2), [3,-6], makeboxc("$\\theta$"))
annotate(prsph(rho/2, phi, th), [1,-5], makeboxc("$\\rho$"))
annotate(pr([A[0]/2, A[1]/2, A[2]]), [0, 3], 
        makeboxc("$\\rho\\sin\\phi$"))
annotate(pr([1,0,0]), [-5, -6], "$x$")
annotate(pr([0,0.7,0]), [-4, -6], "$y$")
annotate(pr([0,0,1.0]), [-5, -8], "$z$")
closeOutputFile()


setViewBox(-0.2, -0.5, 1.25, 1.0) #  Cylindrical coordinates {{{1
openOutputFile("04cylindrical-coordinates", 120)

#the axes  (x green, y red, z blue) {{{1
if draft: linewidth(2)
if draft: setrgbcolor ('green')
line3d ([-0.5,0,0], [1,0,0])
if draft: setrgbcolor ('red')
line3d([0,-0.5,0], [0,0.7,0])
if draft: setrgbcolor ('blue')
line3d([0,0,0], [0,0,1.0])
if draft: linewidth(1)

# drawing of the coordinates {{{1
if draft==1: 
    setrgbcolor('eggplant')
A = cyl(r, th, z)
line3d(origin, [A[0],A[1],0])
line3d(A, [A[0],A[1],0])
linewidth(0.4)
drawhorizarc(0,th, pi/2, r/4)
setdash("[3 2 0.5 2] 0")
line3d([A[0],0,0], [A[0],A[1],0])
line3d([0,A[1],0], [A[0],A[1],0])
setdash("[] 0")
roundPoint(pr(A))
#Annotations
annotate(prcyl(r/4, th/2, 0), [3,-6], makeboxl("$\\theta$"))
annotate(prcyl(r/2, th, 0), [0,2], makeboxc("$r$"))
annotate(prcyl(r, th, z/2), [2, 0], makeboxl("$z$"))
annotate(pr([1,0,0]), [-5, -6], "$x$")
annotate(pr([0,0.7,0]), [-4, 3], "$y$")
annotate(pr([0,0,1.0]), [-5, -8], "$z$")
closeOutputFile()


