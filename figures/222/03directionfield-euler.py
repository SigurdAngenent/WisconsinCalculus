#!/usr/bin/python
# Direction field
from math import *
from grapher import *

def slope(x,y):
    return -y+sin(pi*x)

def shoot(xx, yy, dx):
    n=0
    while xx<3.0:
        setrgbcolor("black")
        offset = [-2,3] if yy>0 else [-2, -10]
        PStext([xx,yy], offset, "%s"%(n), "Helvetica-Oblique", 8 )
        m=slope(xx, yy)
        xn=xx+dx
        yn=yy+m*dx
        setrgbcolor("red")
        arrow([xx,yy], [xn,yn], 7, 2, 0)
        roundPoint([xx,yy], 0.05)
        xx,yy = xn, yn
        n+=1

dx = 0.5
dy = 0.25
elementlength = 0.15

setViewBox(-3.1, -3, 3.3, 3.3)
openOutputFile("03directionfield-euler", 240)

axes([7,7])
linewidth(0.4)
setrgbcolor("lightGray")
x= -3.0
while (x<3.1):
    y=-2.5
    while y<3.0:
        m=slope(x,y)
        s=sqrt(1+m*m)
        vx = elementlength/s
        vy = elementlength*m/s
        line([x-vx, y-vy], [x+vx, y+vy])
        roundPoint([x,y])
        y+=dy
    x+=dx

setrgbcolor("red")
linewidth(1)
shoot(-2.5, 3.0, dx)

closeOutputFile()


