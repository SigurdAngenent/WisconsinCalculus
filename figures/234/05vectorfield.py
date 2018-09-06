from grapher import *

def vfx(x, y): #{{{1
    return -y/(0.0+sqrt(x*x+y*y))**2
def vfy(x, y): #{{{1
    return x/(0.0+sqrt(x*x+y*y))**2
setViewBox(-1.0, -0.5, 1.0, 0.5) # {{{1
openOutputFile("05vectorfield", 240)
axes ([0,0])

## Draw the vector field {{{1
s = 0.01 # length scale of vectors
Nx, Ny = 55, 35
Dx = (Viewxmax()-Viewxmin())/Nx
Dy = (Viewymax()-Viewymin())/Ny
xlist = [Viewxmin()+(k+1)*Dx for k in range(Nx-1)]
ylist = [Viewymin()+(k+1)*Dy for k in range(Ny-1)]
linewidth(0.1)
for x in xlist:
    for y in ylist:
        vx, vy = vfx(x,y), vfy(x, y)
        arrow([x, y], [x+s*vx, y+s*vy], 1.5, 0.5)
        #roundPoint([x,y],0.007,fillcolor='black')
        

## ANNOTATIONS {{{1

closeOutputFile() #{{{1


