
#!/usr/bin/python   {{{1
#level curve, tangent, gradient, and directions of increase/decrease

from math import *
from grapher import *

setViewBox(-3.05, -2.05, 3.05, 2.05)  #{{{1
openOutputFile("01steepestdescent", 240)
def f(x):#{{{1
    return 1.0 - exp(x)
def df(x):#{{{1
    return - exp(x)
#{{{1 main
#line([Viewxmin(), 0], [Viewxmax(),0])
#line([0, Viewymin()], [0, Viewymax()])

sqtwo=1.4142135
linewidth(0.25)  #{{{2 the other level curves
setrgbcolor('gray')
setdash("[5 3] 0")
for t in(-2, -1, 1, 2):
    plot(lambda x: x, lambda x: f(x-t)+0.3*t, Viewxmin(), Viewxmax())

#{{{2 the zero set, tangent, gradient, and circle
setrgbcolor('black')
setdash("[] 0")
linewidth(1)
plot(lambda x:x, f, Viewxmin(), Viewxmax())
line([-2,2], [2, -2])
arrow([0,0], [sqtwo,sqtwo], 7,2)
linewidth(0.5)
arc([0,0], sqtwo, [0,360])

#{{{2 Annotations
annotate([sqtwo,sqtwo], [2,2], makeboxl("$\\nab f(P)$"))
annotate([-3,f(-3)], [-4,-1], makeboxr("f = 0.0"))
for t in(-2, -1, 1, 2):
    annotate([-3, f(-3.0 - t)+0.3*t], [-4,-1], 
            makeboxr("%2.1f"%(0.3*t)))
A,B,C,D = [1,1], [-1,1], [1, -1], [-1,-1]
roundPoint(A)
annotate(A, [-5,-3], makeboxr("$A$"))
roundPoint(B)
annotate(B, [-3,-3], makeboxr("$B$"))
roundPoint(C)
annotate(C, [0,-10], makeboxc("$C$"))
roundPoint(D)
annotate(D, [-1,-8], makeboxr("$D$"))
roundPoint([0,0])
annotate([0,0], [-3,-10], makeboxr("$P$"))
closeOutputFile()


