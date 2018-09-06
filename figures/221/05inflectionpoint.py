#Time-stamp: Thu Oct 18 12:27:43 CDT 2007 angenent

from grapher import *
from math import *

def x(t): return t
def y(t): return t-t*t*t
#setViewBox, openOutputFile
setViewBox(-1.5, -1.0, 1.5, 1.0)
openOutputFile("05inflectionpoint", 90)

    #polygonA([[Viewxmin()+0.1,Viewymax()-0.1],
          #[Viewxmin()+0.1,Viewymin()+0.1],
          #[Viewxmax()-0.1,Viewymin()+0.1]])

#the graph
plot(x,y, -1.2, 1.2)
setrgbcolor('blue')
line([-1, -1], [1, 1])
roundPoint([0,0])
#annotations
annotate([-1.1,0.3], [2,0], r"\footnotesize$f''(x)>0$")
annotate([1, 0], [3,2], r"\footnotesize$f''(x)<0$")
closeOutputFile()


