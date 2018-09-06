
from math import *
from grapher import *


setViewBox(-3,-3,3,3) #{{{1
openOutputFile("03answers006", 80)

def hype(a, sx, sy):
    plot(lambda t: sx*exp(t-a),
         lambda t : sy*exp(-t-a),
         -a-log(3), a+log(2.5))

    

linewidth(0.8)
plot(lambda t: cos(t), lambda t : 2*sin(t), 0, 2*pi)
linewidth (0.4)
setrgbcolor ('blue')
for a in (0, 0.5, 1.0, -0.5):
    hype(a, 1, 1)
    hype(a, -1, -1)
setrgbcolor ('red')
for a in (0, 0.5, 1.0, -0.5):
    hype(a, -1, 1)
    hype(a, 1, -1)
setrgbcolor ('black')
axes([6,6])

a=sqrt(2)
b=1/a
linewidth (0.4)
roundPoint ([b,a], 0.05)
roundPoint ([-b,a], 0.05)
roundPoint ([b,-a], 0.05)
roundPoint ([-b,-a], 0.05)

PStext ([b,a], [2,0], 'A', 'Helvetica-Oblique',7)
PStext ([-b,a], [-6,0], 'B', 'Helvetica-Oblique',7)
PStext ([-b,-a], [-6,-6], 'C', 'Helvetica-Oblique',7)
PStext ([b,-a], [0,-6], 'D', 'Helvetica-Oblique',7)
closeOutputFile()  # Done {{{1


