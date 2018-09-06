#!/usr/bin/python
# Direction field
from math import *
from grapher import *

def slope(x,y):
    return -y+sin(pi*x)

def shoot(xx, yy, h):
    points=[(xx, yy)]
    while xx<3.0:
        m=slope(xx, yy)
        mm=slope(xx+h, yy+m*h)
        xx+=h
        yy+=(m+mm)*h/2
        points.append((xx,yy))
    polygonA(points)

dx = 0.5
dy = 0.25
elementlength = 0.15

setViewBox(-3.1, -3, 3.3, 3.3)
openOutputFile("03directionfield-withsolutions", 240)

axes([7,7])
linewidth(0.25)
setrgbcolor("cayenne")
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
x=-3.0
while x<3.0:
    shoot (x, 3.0, dx/10)
    x+=dx/4
setrgbcolor("teal")
x=-3.0
while x<3.0:
    shoot (x, -3.0, dx/10)
    x+=dx/4
setrgbcolor("orange")
y=3.0-dy
while y>-3.0:
    shoot (-3.0, y, dx/10)
    y-=dy

closeOutputFile()


