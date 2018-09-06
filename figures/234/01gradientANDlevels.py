#!/usr/bin/python   {{{1
#level curves of some function with gradients drawn

from math import *
from grapher import *

setViewBox(-3, -2, 3, 2)  #{{{1
openOutputFile("01gradientANDlevels", 180)

def x(t): #{{{1
    return t*(1-t*t)
def y(t): #{{{1
    return 1-t*t
def drawgradf(t): #{{{1
    s=0.25
    xx, yy = x(t), y(t)
    grx, gry = 2*xx, (3*yy-2)*yy
    print( "t=%5f xx=%5f yy=%5f grad=(%5f, %5f)"%(t, xx, yy, grx, gry) )
    arrow([xx, yy], [xx+s*grx, yy+s*gry], 3, 2)
    
def annotategradf(t): #{{{1
    s=0.25
    xx, yy = x(t), y(t)
    grx, gry = 2*xx, (3*yy-2)*yy
    roundPoint([xx, yy], 0.04)
    annotate([xx, yy], [0, -10], makeboxl("$(a,b)$"))
    annotate([xx+s*grx, yy+s*gry], [0,4], makeboxc("$\\nab f(a,b)$"))
    
#{{{1 main
linewidth(0.25)
line([Viewxmin(), 0], [Viewxmax(),0])
line([0, Viewymin()], [0, Viewymax()])

linewidth(1.0)
setrgbcolor('UWBadgerRed')
drawgradf(0)
linewidth(0.5)
setrgbcolor('gray')
for t in (0.25, 0.5, 0.7, 0.85, 1.1, 1.2, 1.3, 1.4, 1.5):
    drawgradf(t)
    drawgradf(-t)

linewidth(1)
setrgbcolor('black')
plot(x, y, -2, 2)


annotate([x(-1.6), y(-1.6)], [0, 2], makeboxl(r"$f(x, y) = 0$"))
annotate( [0,1.25] , [1,1] , makeboxl(r"\color{badgerred}$\nab f(0,1)$") )
annotategradf(1.5)

closeOutputFile()


