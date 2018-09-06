from math import *
from numpy import *
from grapher import *

def rotatex(angle,pro): #{{{1
    c, s = cos(angle), sin(angle)
    return matrix([[1,0,0], [0,c, -s], [0, s, c]])*pro
def rotatey(angle,pro): #{{{1
    c, s = cos(angle), sin(angle)
    return matrix([[c, 0, -s], [0,1,0], [s, 0, c]])*pro
def rotatez(angle,pro): #{{{1
    c, s = cos(angle), sin(angle)
    return matrix([[c,-s,0], [s, c, 0], [0,0,1]]) * pro
def pr(q): #{{{1
    """ Multiply the row matrix q with PMAT and return as list"""
    global PMAT
    qq = q*PMAT
    return [qq[0,0], qq[0,1]]

def line3d(P,Q): #{{{1
    line(pr(matrix(P)), pr(matrix(Q)))
def shadowlines3d(segmentlist,widths=[1,0.25]): #{{{1
    setrgbcolor('white')
    linewidth(widths[0])
    for seg in segmentlist:
        line3d(seg[0],seg[1])
    setrgbcolor('black')
    linewidth(widths[1])
    for seg in segmentlist:
        line3d(seg[0],seg[1])

def tower(x0, y0, x1, y1, h): #{{{1
    outline = [[x1, y0, 0],
               [x1, y1, 0],
               [x0, y1, 0],
               [x0, y1, h],
               [x0, y0, h],
               [x1, y0, h],
               [x1, y0, 0]]
    outline = [pr(p) for p in outline]
    frontedges=[ [[x1, y0, h],[x1,y1,h]],
                 [[x0, y1, h],[x1,y1,h]],
                 [[x1,y1,h],[x1,y1,0]] ]
    setrgbcolor('white')
    polygonF(outline)
    setrgbcolor('black')
    polygonA(outline)
    for edge in frontedges:
        line(pr(edge[0]), pr(edge[1]))

#  Set rotation matrix {{{1
PMAT = matrix( [[0,0], [1,0], [0,1]] )
PMAT = rotatey(pi/10, PMAT)
PMAT = rotatez(pi/6, PMAT)
print( PMAT )

## def fun(x, y): return x*x*exp(-1-0.7*y) #{{{1
def fun(x, y): return x*x/(2+4*y) #{{{1
# The Domain
x0,x1 = -3.0, -1.0
y0,y1 = 0.5, 2.0

def riemannsum(N,M, label, lw=0.4): #{{{1
    global x0, x1, y0, y1
    setViewBox(-1,-2,4,4) #{{{2
    openOutputFile("04riemannsum"+label, 150)
    # The axes. {{{2
    linewidth(1)
    line3d([-7,0,0], [1,0,0])
    line3d([0,-1,0], [0,3,0])
    line3d([0,0,0], [0,0,4])
    # Lines delimiting the domain
    linewidth(2*lw)
    line3d([x0,0,0], [x0,y1+0.5,0])
    line3d([x1,0,0], [x1,y1+0.5,0])
    line3d([0, y0, 0], [x0-0.5, y0, 0])
    line3d([0, y1, 0], [x0-0.5, y1, 0])
    # Draw the towers {{{2
    linewidth (lw)
    x=x0
    dx=(x1-x0)/N
    dy=(y1-y0)/M
    while x<x1-0.00001:
        y=y0
        while y<y1-0.00001:
            tower(x, y, x+dx, y+dy, fun(x,y))
            y+=dy
        x+=dx
    # Annotations {{{2
    annotate(pr([-7, 0, 0]), [0,3], r"$y$")
    annotate(pr([0.0, 3, 0]), [3,-6], r"$x$")
    annotate(pr([0, 0, 4]), [0,2], makeboxc("$z$"))
##    annotate(pr([2.0, 2.0, 0.0]), [0,-7], makeboxl("N=%d"%(N)))
##    annotate(pr([3.0, 1.25, 0.0]), [-3,-5], makeboxr("M=%d"%(M)))
    closeOutputFile()

def oneslice(N,M, label, lw=0.4): #{{{1
    setViewBox(-1,-0.5,4,2) #{{{2
    openOutputFile("04riemannsumslice"+label, 250)
    # The axes. {{{2
    linewidth(1)
    line3d([-6,0,0], [1,0,0])
    line3d([0,-1,0], [0,3,0])
    line3d([0,0,0], [0,0,2])
    # Lines delimiting the domain
    linewidth(0.4)
    line3d([x0,0,0], [x0,y1+0.5,0])
    line3d([x1,0,0], [x1,y1+0.5,0])
    line3d([0, y0, 0], [x0-0.5, y0, 0])
    line3d([0, y1, 0], [x0-0.5, y1, 0])
    # The domain {{{2
    polygonF([pr([x0,y0, 0]),
            pr([x0,y1, 0]),
            pr([x1,y1, 0]),
            pr([x1,y0, 0]),
            pr([x0,y0, 0]),],
            [198,198,198])
    # The slices {{{2
    linewidth(lw)
    dx= (x1-x0)/N
    dy= (y1-y0)/M
    xm = x0 + (N/2) * dx
    ym = y0 + (M/2) * dy
    y=y0
    while y<y1-0.0001:
        tower(xm, y, xm+dx, y+dy, fun(xm,y))
        y+=dy
    # Annotations {{{2
    annotate(pr([-6, 0, 0]), [0,3], r"$y$")
    annotate(pr([0.0, 3, 0]), [3,-6], r"$x$")
    annotate(pr([0, 0, 2]), [0,2], makeboxc("$z$"))
    annotate(pr([0, y0, 0]), [0,-8], makeboxr("$x=a$"))
    annotate(pr([0, y1, 0]), [0,-8], makeboxr("$x=b$"))
    annotate(pr([x0, y1+0.5, 0]), [2,-3], makeboxl("$y=d$"))
    annotate(pr([x1, y1+0.5, 0]), [2,-3], makeboxl("$y=c$"))
    closeOutputFile()

# Main program {{{1
#riemannsum(1, 1, "crude")
riemannsum(4, 3, "coarse",lw=0.2)
riemannsum(30, 20, "medium", lw=0.1)
oneslice(30, 20, "fine")

