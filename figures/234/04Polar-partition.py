from math import *
from grapher import *
## Parameters {{{1
rmin=0.4
rmax=1.3
thmin=15.0
thmax=120.0
nr = 5
nth=6
dr = (rmax-rmin)/nr
dth= (thmax-thmin)/nth

def drawarc(r): #{{{1
    global thmin, thmax
    arc([0,0], r, [thmin, thmax])

def drawspoke(th): #{{{1
    global rmin, rmax
    th = th*pi/180
    line([rmin*cos(th), rmin*sin(th)], [rmax*cos(th), rmax*sin(th)])

setViewBox(-1,-0.2,2,2) #{{{1
openOutputFile("04Polar-partition", 150)

axes([7,7])
drawarc(rmin)
drawarc(rmax)
drawspoke(thmin)
drawspoke(thmax)

linewidth(0.4)

for i in range(nr-1):
    drawarc(rmin+(i+1)*dr)

for i in range(nth-1):
    drawspoke(thmin+(i+1)*dth)

annotate([1.9,0], [0,2], "$x$")
annotate([0,1.8], [3,0], "$y$")
closeOutputFile()

