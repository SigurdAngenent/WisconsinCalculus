from math import *
from grapher import *
import random

def l(x) : return 0.3*x+0.5#{{{1

def datapoint(x,y,rad=0.02): #{{{1
    setrgbcolor('red')
    setdash("[3 4] 0")
    line([x, l(x)], [x, y])
    setdash("[] 0")
    setrgbcolor('cayenne')
    roundPoint([x,y], rad) 

setViewBox(-0.5, -0.5, 6, 3) #{{{1
openOutputFile("02linearregression", 300)

axes()#{{{1
setrgbcolor('blue')
a=-0.5 #{{{1
b=5.8
line([a,l(a)], [b, l(b)])

for i in range(21):
    x=random.random()

setrgbcolor('red')
for i in range(40):
    x=5*random.random() - 0.5
    y=random.normalvariate(l(x), 0.3) 
    datapoint(x, y)

#line([4, 0], [4,2])
setrgbcolor('cayenne')
linewidth(2)
datapoint(4,l(4)-1, 0.04)


annotate([4.75, l(4.75)], [0,4],
         makeboxl(r"\rotatebox{%lf}{$y=ax+b$}"%(atan(0.3)*180/pi)    ))
annotate([4, l(4)-1], [0, -10], makeboxc("$(x_k, y_k)$"))
annotate([4, l(4)-0.5], [4,0], makeboxl(r'$\bigl|ax_k+b-y_k\bigr|$'))
closeOutputFile()


