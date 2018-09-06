from grapher3d import *
draft=0
###  set projection matrix     {{{1

setProjection(rotatey(pi/9, theProjection ()))
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
def drawhorizarcA(th0, th1, phi, rho, N=11): #{{{1
    thstep = (th1-th0)/(N-1.0)
    polygonA([prsph(rho, phi, th0+j*thstep) for j in range(N)])
def drawhorizarcF(th0, th1, phi, rho, N=11): #{{{1
    thstep = (th1-th0)/(N-1.0)
    polygonF([prsph(rho, phi, th0+j*thstep) for j in range(N)], 'gray')

setViewBox(-1.5, -1.7, 1.5, 1.7) # {{{1
openOutputFile("04integral-over-sphere", 200)

#the axes  (x green, y red, z blue) {{{1
linewidth(0.5)
if draft: linewidth(2)
if draft: setrgbcolor ('green')
line3d ([-2,0,0], [1.5,0,0])
if draft: setrgbcolor ('red')
line3d([0,-1.5,0], [0,1.5,0])
if draft: setrgbcolor ('blue')
line3d([0,0,-1.5], [0,0,0.5])
if draft: linewidth(1)

## Set parameters, th, phi, rho {{{1
origin = [0,0,0]
th=pi/4  ## theta {{{2
dth=pi/24
thk = pi/4
phi=5*pi/24  ## phi {{{2
dphi=pi/48
rho=1.2  ## rho {{{2
drho=0.1
A= sph(1, pi/3, thk)
AA = [A[0], A[1], 0]
B= sph(1, pi/3, pi-thk)
BB = [B[0], B[1], 0]
# The slices {{{1
if draft==1: 
    setrgbcolor('eggplant')
arc([0,0], 1, [0, 360])
drawhorizarcA(0, 2*pi, pi/2, 1, 101)
drawhorizarcA(0, 2*pi, pi/2, sin(pi/3), 101)
polygonF([pr(x) for x in(A, B, BB, AA, A)], [200,200,200])
linewidth(1)
drawhorizarcF(0, 2*pi, pi/3, 1, 101)
linewidth(1.5)
line3d(A, B)
linewidth(0.5)
line3d([0,0,0.5], [0,0,1.5])
# Annotations {{{1
annotate(pr([0,0,1.5]), [2, 0], "$z$")
annotate(pr([0,1.5,0]), [0, 3], "$y$")
annotate(pr([1.5,0,0]), [3, 0], "$x$")
closeOutputFile()

