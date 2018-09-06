#! /usr/bin/python
# Time-stamp: <2012-07-13 10:38:53 angenent>
from grapher import *
from math import *

setViewBox(-2*pi,-1.2,2*pi,1.6)
openOutputFile("03sinx-over-x",270)
axes([5,5])

n=300
xx = [k*1.8*pi/n for k in range(1, n+1)]
grright = [(x, sin(x)/x) for x in xx]
gr = [(-g[0], g[1]) for g in grright]
gr.reverse()
gr.append((0,1))
gr.extend(grright)
polygonA(gr)
roundPoint([0,1], 0.1)
linewidth(0.3)
arrow([1.0, -0.5], [0.08, 0.9], 7, 2)
annotate([1.0, -0.5], [1, -8],
         makeboxl(r"\footnotesize the missing point in the graph"))
annotate([-pi, 1], [0,0],
         makeboxc(r"\footnotesize $y=\dfrac{\sin x}{x}$ $(x\neq0)$") )
closeOutputFile()


