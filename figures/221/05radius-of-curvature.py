#!/usr/bin/python
## Time-stamp: <2012-07-10 12:09:35 angenent>

from grapher import *
from math import *

def f(t): return sqrt(0.2+t*t)/sqrt(1.2)

setViewBox(-3,-0.1, 3, 4)
openOutputFile("05radius-of-curvature",240)

cx, cy = 0.0, 2.0
rad = 2.0
wl, wr = 0.5, 2.0
th0, th1 = 0.2*pi , 0.3*pi
phi0, phi1 = th0*180/pi-90, th1*180/pi-90
th2 = (th0+th1)*0.5
rad2 = rad/cos(0.5*(th1-th0))
px, py = cx+rad*sin(th0), cy-rad*cos(th0)
qx, qy = cx+rad*sin(th1), cy-rad*cos(th1)
rx, ry = cx+rad2*sin(th2), cy-rad2*cos(th2)
sx, sy = rx+0.7*wr*cos(th2), ry+0.7*wr*sin(th2)
tx, ty = cx+rad*sin(th1)/4, cy-rad*cos(th1)/4
ux, uy = cx+rad*sin(th2)*0.6, cy-rad*cos(th2)*0.6

th = [k*pi/100 for k in range(-45,120)]
pc = [(rad*f( 1 + 0.5*(t-th0) * (t-th1)**2 ) , t) for t in th]
po = [(cx + p[0]*sin(p[1]), cy - p[0]*cos(p[1])) for p in pc]

setrgbcolor ('red')
linewidth (2)
polygonA (po)
setrgbcolor ('black')
arc([cx, cy], rad, [phi0, phi1])

linewidth (0.3)
arc([cx, cy], rad, [0, 360])
line([px-wl*cos(th0), py-wl*sin(th0)], [px+wr*cos(th0), py+wr*sin(th0)])
line([qx-wl*cos(th1), qy-wl*sin(th1)], [qx+0.8*wr*cos(th1), qy+0.8*wr*sin(th1)])
polygonA([[px,py], [cx,cy], [qx,qy]])
arc([rx,ry], wr*0.7, [th0*180/pi, th1*180/pi])
arc([rx,ry], wr*0.71, [th0*180/pi, th1*180/pi])
arc([cx,cy], rad*0.52, [th0*180/pi-90, th1*180/pi-90])
arc([cx,cy], rad*0.53, [th0*180/pi-90, th1*180/pi-90])

linewidth(0.5)
roundPoint([px, py])
roundPoint([qx, qy])

#polygonF( rect(ux-0.3, ux+0.1, uy-0.02, uy+0.1) , "white")

annotate ([ux,uy], [0,-1], makeboxc("$\gamma$"))
annotate ([rx,ry], [0, -10], "$\Delta s$")
annotate ([sx,sy], [0,2], "$\Delta\\alpha$")
annotate ([cx,cy], [-2, 0], makeboxr("$C$"))
annotate ([tx,ty], [5,0], rotatebox(th1*180/pi-90, "radius $=R$"))
annotate ([px,py], [-3,-1], makeboxr ("$P$"))
annotate ([qx,qy], [-3,-1], makeboxr ("$Q$"))
closeOutputFile()




