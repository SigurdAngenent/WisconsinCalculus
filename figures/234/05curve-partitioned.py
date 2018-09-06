from grapher import *

def lissajous(t): #{{{1
    t+=0.5
    return [cos(t), 0.5*sin(2*t)]
def lissnormal(t): #{{{1
    t+=0.5
    vx, vy = cos(2*t), sin(t) 
    nm = sqrt(vx*vx+vy*vy)
    return [vx/nm, vy/nm]

setViewBox(-1.2, -0.7, 1.2, 0.7) # {{{1
openOutputFile("05curve-partitioned", 120)

## Draw the curve segments {{{1
linewidth(4)
setlinecap(0)
for j in range(10, 200, 20):
    curve = [lissajous(0.01*k*pi) for k in range(j, j+11)]
    polygonA(curve)
setrgbcolor([128, 255, 128])
for j in range(0, 200, 20):
    curve = [lissajous(0.01*k*pi) for k in range(j, j+11)]
    polygonA(curve)
## MARK ONE SEGMENT {{{1
setrgbcolor('black')
linewidth(0.5)
setlinecap(1)
m = -20
a = lissajous(0.01*m*pi)
b = lissajous(0.01*(m+10)*pi)
nma = lissnormal(0.01*m*pi)
nmb = lissnormal(0.01*(m+10)*pi)
c = [a[0]+0.3*nma[0], a[1]+0.3*nma[1]]
d = [b[0]+0.3*nmb[0], b[1]+0.3*nmb[1]]
cc= [a[0]-0.2*nma[0], a[1]-0.2*nma[1]]
dd= [b[0]-0.2*nmb[0], b[1]-0.2*nmb[1]]
line(cc, c)
line(dd, d)
## ANNOTATIONS {{{1
annotate(lissajous(0.01*(m+5)*pi), [4,-2], "$\\updownarrow\\Delta s$")
closeOutputFile() #{{{1


