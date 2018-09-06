from grapher3d import *
draft=0
###  set projection matrix     {{{1

setProjection(rotatey(pi/7, theProjection ()))
setProjection(rotatez(-pi/20, theProjection ()))

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

setViewBox(-0.2, -0.5, 0.75, 1) # {{{1
openOutputFile("04spherical-block", 150)

#the axes  (x green, y red, z blue) {{{1
if draft: linewidth(2)
if draft: setrgbcolor ('green')
line3d ([-0.5,0,0], [1,0,0])
if draft: setrgbcolor ('red')
line3d([0,-0.5,0], [0,0.75,0])
if draft: setrgbcolor ('blue')
line3d([0,0,0], [0,0,1])
if draft: linewidth(1)
def drawbox(rho, drho, phi, dphi, th, dth, lwthin, lwthick): # {{{1
    # compute trig functions: {{{2
    cth = cos(th)
    sth = sin(th)
    cth2= cos(th+dth)
    sth2= sin(th+dth)
    cphi=cos(phi)
    sphi=sin(phi)
    cphi2=cos(phi+dphi)
    sphi2=sin(phi+dphi)
    # start drawing: {{{2
    linewidth(lwthin)
    line3d(sph(rho-drho, phi, th), sph(rho, phi, th))
    drawvertarc(th, phi, phi+dphi, rho)
    drawvertarc(th+dth, phi, phi+dphi, rho)
    drawhorizarc(th, th+dth, phi+dphi, rho)
    line3d(sph(rho-drho, phi+dphi, th+dth), sph(rho, phi+dphi, th+dth))
    line3d(sph(rho-drho, phi, th+dth), sph(rho, phi, th+dth))
    drawhorizarc(th, th+dth, phi+dphi, rho-drho)
    drawhorizarc(th, th+dth, phi, rho)
    drawvertarc(th+dth, phi, phi+dphi, rho-drho)
    linewidth(lwthick)
    line3d(sph(rho-drho, phi+dphi, th), sph(rho, phi+dphi, th))
    drawhorizarc(th, th+dth, phi, rho-drho)
    drawvertarc(th, phi, phi+dphi, rho-drho)

## Set parameters, th, phi, rho {{{1
origin = [0,0,0]
th=pi/12  ## theta {{{2
dth=pi/3
phi=2*pi/12  ## phi {{{2
dphi=pi/4
rho=0.7  ## rho {{{2
drho=0.5

# The box {{{1
if draft==1: 
    setrgbcolor('eggplant')
drawbox(rho, drho, phi, dphi, th, dth, 0.6, 0.6)
linewidth(0.5)

A = sph(rho-drho, phi, th)
B = sph(rho-drho, phi, th+dth)
line3d(origin, A)
#line3d([0,0,A[2]], A) 
line3d(origin, B)
#line3d([0,0,B[2]], B)
line3d(origin, sph(rho-drho, phi+dphi, th))
line3d(origin, sph(rho-drho, phi+dphi, th+dth))
linewidth(0.1)
drawhorizarc(0, pi/2, phi, rho, 51)
drawhorizarc(0, pi/2, pi/2, rho, 51)
drawhorizarc(0, pi/2, phi+dphi, rho, 51)
drawvertarc(0, 0, pi/2, rho, 51)
drawvertarc(pi/2, 0, pi/2, rho, 51)
drawvertarc(th, 0, pi/2, rho, 51)
drawvertarc(th+dth, 0, pi/2, rho, 51)
for j in range(1,80):
    line3d(sph(rho-drho, phi+j*0.0125*dphi, th),
           sph(rho, phi+j*0.0125*dphi, th))
    drawvertarc(th, phi, phi+dphi, rho-j*0.0125*drho)
    drawhorizarc(th, th+dth, phi+j*0.0125*dphi, rho)
# Annotations {{{1
closeOutputFile()


