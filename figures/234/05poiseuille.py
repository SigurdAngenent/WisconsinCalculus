from grapher import *

def vfx(x, y): #{{{1
    return 0.25-y*y
def vfy(x, y): #{{{1
    return 0
setViewBox(-1.2, -0.6, 1.2, 0.65) # {{{1
openOutputFile("05poiseuille", 200)
## The axes {{{1
setdash("[3 1 0.5 1] 0")
linewidth(0.6)
setrgbcolor('midnight')
line([Viewxmin(), 0], [Viewxmax(),0])
setdash("[] 0")
arrow([0,0], [0, 0.6], len=6, wid=2)
## The walls {{{1
linewidth(2)
setrgbcolor('gray')
for y in (-0.5, 0.5):
    line([-1, y], [1, y])
setrgbcolor('black')
## Draw the vector field {{{1
s = 0.55 # length scale of vectors
Nx, Ny = 11, 15
xmin, xmax = -0.9, 0.9
ymin, ymax = -0.5, 0.5
Dx = (xmax-xmin)/Nx
Dy = (ymax-ymin)/Ny
xlist = [xmin+(k)*Dx for k in range(Nx)]
ylist = [ymin+(k)*Dy for k in range(Ny+1)]
linewidth(0.3)
for x in xlist:
    for y in ylist:
        vx, vy = vfx(x,y), vfy(x, y)
        if (vx*vx+vy*vy > 0.0001):
            arrow([x, y], [x+s*vx, y+s*vy], 2, 0.7)
        roundPoint([x,y],0.003,fillcolor='black')

## ANNOTATIONS {{{1
annotate([1.0, 0], [0, 2], "central axis")
annotate([0, 0.55], [4, 0], "$r$")
annotate([1.0, 0.55], [2, -6], "wall")

closeOutputFile() #{{{1


