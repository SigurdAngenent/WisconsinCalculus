from math import *
from doodler import *

def degrees(rads): return rads/pi*180
z=1.5
setViewBox(-z, -z, z, z)
openOutputFile("02string-around-earth", 200, r"\usepackage{mathpazo}")


theta=0.7 # radians
O= [0,0]
A= [sin(theta), cos(theta)]
B= [0, 1.0/cos(theta)]
C= [-A[0], A[1]]
D= [0,1]
polygonA([C, B, A])
arc ([0,0], 1, [degrees(pi/2 + theta),degrees (pi/2 - theta)])
linewidth(0.5)
setrgbcolor('blue')
arc ([0,0], 1, [degrees(pi/2 - theta),degrees (pi/2 + theta)])
arc ([0,0], 0.3, [degrees(pi/2 - theta), 90])
arc ([0,0], 0.32, [degrees(pi/2 - theta), 90])
polygonA([C, O, A])
line(O, B)

setrgbcolor('black')
for P in [O,A,B,C,D]:
    roundPoint(P, 0.02)
annotate(O, [2, -5], makeboxl("$O$"))
annotate(A, [2,  0], makeboxl("$A$"))
annotate(B, [2,  0], makeboxl("$B$"))
annotate(C, [-2, 0], makeboxr("$C$"))
annotate(D, [2, -9], makeboxl("$D$"))
annotate([0.1,0.33], [0, 0], makeboxl ("$\\theta$"))
annotate([0,-0.6], [0,0], makeboxc (r"$AB-AD = $ ???"))

closeOutputFile()
