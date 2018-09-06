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

setViewBox(-0.5, -0.50, 1.25, 1.7) # {{{1
openOutputFile("04spherical-volume-element", 150)

#the axes  (x green, y red, z blue) {{{1
if draft: linewidth(2)
if draft: setrgbcolor ('green')
line3d ([-0.5,0,0], [1,0,0])
if draft: setrgbcolor ('red')
line3d([0,-0.5,0], [0,1,0])
if draft: setrgbcolor ('blue')
line3d([0,0,0], [0,0,1.7])
if draft: linewidth(1)
def drawbox(rho, drho, phi, dphi, th, dth, dashends=1): # {{{1
    cth = cos(th)
    sth = sin(th)
    cth2= cos(th+dth)
    sth2= sin(th+dth)
    cphi=cos(phi)
    sphi=sin(phi)
    cphi2=cos(phi+dphi)
    sphi2=sin(phi+dphi)
    setdash("[] 0")
    linewidth(0.6)
    line3d(sph(rho-drho, phi, th), sph(rho, phi, th))
    line3d(sph(rho-drho, phi+dphi, th), sph(rho, phi+dphi, th))
    drawvertarc(th, phi, phi+dphi, rho)
    drawvertarc(th+dth, phi, phi+dphi, rho)
    drawhorizarc(th, th+dth, phi+dphi, rho)
    drawvertarc(th, phi, phi+dphi, rho-drho)
    if dashends==1:
        setdash("[1 1] 0")
        linewidth(0.3)
    line3d(sph(rho-drho, phi+dphi, th+dth), sph(rho, phi+dphi, th+dth))
    line3d(sph(rho-drho, phi, th+dth), sph(rho, phi, th+dth))
    drawhorizarc(th, th+dth, phi+dphi, rho-drho)
    drawvertarc(th+dth, phi, phi+dphi, rho-drho)
    if dashends==1:
        setdash("[] 0")

## Set parameters, th, phi, rho {{{1
origin = [0,0,0]
th=pi/4  ## theta {{{2
dth=pi/24
phi=5*pi/24  ## phi {{{2
dphi=pi/48
rho=1.2  ## rho {{{2
drho=0.1

# The boxes {{{1
if draft==1: 
    setrgbcolor('eggplant')
phi1=0
while phi1<pi/2.001:
    drawbox(rho, drho, phi1, dphi, th, dth)
    phi1+=dphi
drawhorizarc(0, th, pi/2, rho/3)

A = sph(rho-drho, phi, th)
B = sph(rho-drho, phi, th+dth)
line3d(origin, A)
line3d([0,0,A[2]], A) 
line3d(origin, B)
line3d([0,0,B[2]], [0.85*B[0], 0.85*B[1], B[2]]) 
line3d(B, [0.95*B[0], 0.95*B[1], B[2]]) 
line3d(origin, sph(rho-drho, phi+dphi, th))
line3d(origin, sph(rho-drho, phi+dphi, th+dth))
linewidth(0.1)
setrgbcolor("UWBadgerRed")
for j in range(1,20):
    drawvertarc(th, phi, phi+dphi, rho-j*0.05*drho)
    drawhorizarc(th, th+dth, phi+j*0.05*dphi, rho)
setrgbcolor("black")
line3d(origin,sph(rho-drho, pi/2, th))
line3d(origin,sph(rho-drho, pi/2, th+dth))
drawvertarc(th, 0, phi, rho/3)
# Annotations {{{1
annotate(prsph(0.5*rho, phi, th), [-2,0], makeboxr("$\\rho$"))
annotate(prsph(rho/3, phi/2, th), [3,3], makeboxc("$\\phi$"))
annotate(prsph(rho/3, pi/2, th/2), [5, -3], makeboxl("$\\theta$"))
closeOutputFile()

