from grapher import *

def vfx(x, y): #{{{1
    return 2.0/(2.0+x)
def vfy(x, y): #{{{1
    return sin(pi*x)-y
setViewBox(-1.0, -0.5, 1.0, 0.5) # {{{1
openOutputFile("05flux-across-closed-curve", 240)
axes ([0,0])

# Draw the contour {{{1
Nt = 200
Nn = 4
dt = 2*pi/Nt
tt=[k*dt for k in range(Nt+1)]
contour = [( 0.6*cos(t) - 0.3*cos(3*t) , 0.3*sin(t)+0.1*sin(2*t) ) for t in tt]
linewidth(1)
setrgbcolor('grey90')
polygonF( contour )
setrgbcolor('UWBadgerRed')
polygonC( contour )
# Draw the normals {{{1
for k in range(Nn):
    p = contour[k*Nt/Nn-1]
    q = contour[k*Nt/Nn+1]
    Tang = (q[0]-p[0], q[1]-p[1])
    Norm = (Tang[1], -Tang[0])
    Nlen = 5*sqrt( Norm[0]*Norm[0] + Norm[1]*Norm[1] )
    Norm = (Norm[0]/Nlen, Norm[1]/Nlen)
    arrow( p, (p[0]+Norm[0], p[1]+Norm[1]) )


## Draw the vector field {{{1
s = 0.03 # length scale of vectors
Nx, Ny = 30,15
Dx = (Viewxmax()-Viewxmin())/Nx
Dy = (Viewymax()-Viewymin())/Ny
xlist = [Viewxmin()+(k+1)*Dx for k in range(Nx-1)]
ylist = [Viewymin()+(k+1)*Dy for k in range(Ny-1)]
linewidth(0.1)
setrgbcolor('slateblue')
for x in xlist:
    for y in ylist:
        vx, vy = vfx(x,y), vfy(x, y)
        arrow([x, y], [x+s*vx, y+s*vy], 2.5, 0.5)
        #roundPoint([x,y],0.007,fillcolor='black')
## ANNOTATIONS {{{1

closeOutputFile() #{{{1


