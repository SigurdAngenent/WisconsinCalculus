
from math import *
from grapher import *

def x(t): return sqrt(18.0)*sin(t)
def y(t): return 9*sin(2*t)

setViewBox(-5,-11,5.5,11) #{{{1
openOutputFile("03answers003", 80)

linewidth(0.8)
axes([6,6])
plot(x, y, 0, 2*pi)

h=11
w=h/(3*sqrt(2.0))
setrgbcolor ('red')
#linewidth(0.4)
line([-w,h], [w, -h])
line([-w,-h], [w, h])
setrgbcolor('black')
#linewidth(0.8)
roundPoint([-3,0], 0.15)
roundPoint([ 3,0], 0.15)
roundPoint([ 0,0], 0.15)

PStext([-3,0], [-1,2], '-3', font='Helvetica-Oblique', size=7)
PStext([3,0], [0,2], '3', font='Helvetica-Oblique', size=7)
closeOutputFile()  # Done {{{1


