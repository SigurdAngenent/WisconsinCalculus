#!/usr/bin/python
## Time-stamp: Tue Jun  3 12:23:43 CDT 2008 angenent
from grapher import *
from math import *


setViewBox(-0.2,-0.2, 2.2, 1.7)
openOutputFile("04prodRulePicture",200)

a=1.6
aa=1.7
b=1.1
bb=1.2

#the drawing
lightgrey = [200,200,200]
setrgbcolor(lightgrey)
polygonF([[0,b], [a,b], [a,bb], [0,bb], [0,b]])
polygonF([[a,0], [aa,0], [aa,b], [a,b], [a,0]])
setrgbcolor('gray')
polygonF([[a,b], [aa,b], [aa,bb], [a,bb], [a,b]])

setrgbcolor('black')
polygonA([[aa,0], [aa,bb], [0,bb], [0,0], [aa,0]])
line([0,b], [aa, b])
line([a,0], [a, bb])
roundPoint([0,bb], 0.02)
roundPoint([0,b], 0.02)
roundPoint([0,0], 0.02)
roundPoint([a,0], 0.02)
roundPoint([aa,0], 0.02)

#annotations
linewidth(0.5)
annotate([a/2, 0], [0, -12], r"\makebox[0pt][c]{$u$}")
annotate([(a+aa)/2, 0], [0, -12], r"\makebox[0pt][c]{$\Delta u$}")
annotate([0, b/2], [-3, 0], r"\makebox[0pt][r]{$v$}")
annotate([0, (b+bb)/2], [-3, 0], r"\makebox[0pt][r]{$\Delta v$}")

line([(a+aa)/2, b/2], [aa+0.1, bb/2])
line([a/3, (b+bb)/2], [aa/3, bb+0.1])
line([(a+aa)/2, (b+bb)/2], [aa, bb+0.1])
annotate([a/2, b/2], [0, 0], r"\makebox[0pt][c]{$uv$}")
annotate([aa+0.1, bb/2], [2,0], r"\makebox[0pt][l]{$v\Delta u$}")
annotate([aa/3, bb+0.1], [0, 2], r"\makebox[0pt][c]{$u\Delta v$}")
annotate([aa, bb+0.1], [0, 2], r"\makebox[0pt][c]{$\Delta u\Delta v$}")
closeOutputFile()
    

