from grapher import *
from math import *
#
#  Draw a unit circle, the inscribed N-gon and circumscribed N-gon
#
def archi(N):
    setViewBox(-1.5,-1.5, 1.5, 1.5)
    openOutputFile("03archimedes%03d"%(N),180)
    # Compute constants
    hoek = pi/N
    w=cos(hoek)+sin(hoek)*(1J)
    w2= w*w
    tanhoek=tan(hoek)
    coshoek=cos(hoek)
    linewidth(0.5)
    #the circle
    setrgbcolor([128,255,128])
    arc([0,0], 1, [0,360], "fill")
    #the outer polygon
    setrgbcolor('blue')
    p=(1/coshoek)+0J
    outerpol = [[p.real,p.imag]]
    for i in range(N):
        outerpol.append([p.real,p.imag])
        line([0,0], [p.real,p.imag])
        p=p*w2
    polygonC(outerpol)
    #the inner polygon
    setrgbcolor('red')
    p=w
    innerpol = [[p.real,p.imag]]
    for i in range(N):
        innerpol.append([p.real,p.imag])
        line([0,0], [p.real,p.imag])
        p=p*w2
    polygonC(innerpol)
    closeOutputFile()

for N in range(3, 20):
    archi(N)

