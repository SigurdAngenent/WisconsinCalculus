#!/usr/bin/python

from  grapher  import *
from math import *
from random import random

def id(t): return t
def f(x): return cos(x)
def draw_region(a,b, color='black', fmax=1):
  setrgbcolor(color)
  n=200
  dx=(b-a)/200
  frame=[a+i*dx for i in range(n+1)]
  frame = [(x, f(x)) for  x in frame]
  frame.append((b, 0))
  frame.append((a, 0))
  polygonC(frame)
  for k in xrange(4000):
    xx=random()*(b-a)+a
    yy=random()*fmax
    fxx = f(xx)
    if (fxx>0):
      if (yy<fxx):
        roundPoint([xx,yy], radius=0.002, annotation="", fillcolor=color)
    else:
      if (-yy>fxx):
        roundPoint([xx,-yy], radius=0.002, annotation="", fillcolor=color)


setViewBox(-0.5,-1.2, 3.0, 1.2)
openOutputFile("08Integral-posandneg",270)

draw_region(0, pi/2, color='cyan')
draw_region(pi/2, 2.7, color='tangerine')

linewidth(1)
setrgbcolor('black')
x_axis()
plot(id, f,  Viewxmin(), Viewxmax())

line([pi/6, 0.4], [pi/4, 0.8])
line([2.1, 0.5*cos(2.1)], [2.1, 0.4])
annotate([pi/4, 0.8], [2,2], "Area $=A_1>0$")
annotate([1.7, 0.4], [2,2], "Area $=A_2>0$")
roundPoint([0,0], 0.015)
roundPoint([2.7, 0], 0.015)
roundPoint([pi/2, 0], 0.015)
annotate([0,0], [0, -12], "$a$")
annotate([2.7, 0], [-2, 4], "$b$")
annotate([pi/2, 0], [0, 4], "$c$")
annotate([-0.2, -0.7], [0,0], "$\\int_a^b f(x)dx = A_1 - A_2$")

closeOutputFile()


