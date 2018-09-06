# Time-stamp : Tue Jun  3 14:37:55 CDT 2008 angenent
#
from grapher import *
from math import *

setViewBox(-0.1,-0.1,2.4,1.9)
openOutputFile("02triangleareagrowth",180)

a=1.8
b=a*sqrt(3)/2
aa=1.9
bb=aa*sqrt(3)/2

polygonF([[a,0], [aa,0], [a/2+aa-a,b], [a/2,b], [a,0]], 'lightGray')
polygonF([[a/2,b], [a/2+aa-a,b], [aa/2,bb], [a/2,b]], 'gray')

polygonA([[0,0], [a,0], [a/2, b], [0,0]])
polygonA([[0,0], [aa,0], [aa/2, bb], [0,0]])
line([a/2,b], [a/2+aa-a, b])

roundPoint([0,0], 0.015)
roundPoint([a,0], 0.015)
roundPoint([aa,0], 0.015)

linewidth(0.5)
setdash("[2 3] 0")
line([a/2,0], [a/2,b])
setdash("[] 0")
arrowhead([a/2,0], [a/2,b], 6, 1, -1)
arrowhead([a/2,b], [a/2,0], 6, 1, -1)
annotate([a/2, b/2], [2,0], makeboxl('$h$'))
annotate([a/2,0], [0, -10], makeboxc('$x$'))
annotate([a+(aa-a)/2,0], [0, -10], makeboxc(r'$\Delta x$'))

line([aa/2, (2*b+bb)/3], [aa/2+0.1, bb+0.05])
annotate([aa/2+0.1, bb+0.05], [1,1], makeboxl('very small triangle (ignore)'))
line([aa*3/4,bb/2-0.05], [aa*3/4+0.2,bb/2+0.1])
annotate([aa*3/4+0.2,bb/2+0.1], [1, 1], makeboxl('thin parallelogram'))

closeOutputFile()


