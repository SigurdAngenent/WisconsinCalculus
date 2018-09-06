from grapher import *
from math import *

def f(x): return -(x*x-1)*(x+1)
def x(t): return t

a=-1.0
b=1.0/3
c=1.0

setViewBox(-2.0, -1.0, 2.0, 2.0)
openOutputFile("08f-is-given", 120)
axes([7, 7])

linewidth(0.5)
plot(x, f , -2.0, 1.5)

setdash("[2 2] 0")
line([b,0], [b, f(b)])
setdash("[] 0")
for z in (a, b, c):
    roundPoint([z,f(z)], 0.03)
roundPoint([b, 0], 0.03)

annotate([-1.8, f(-1.8)], [1,1], r"$y=f(x)$")
annotate([a, 0], [0, -10], r"$a$")
annotate([b, 0], [0, -10], r"$b$")
annotate([c, 0], [3,   2], r"$c$")
closeOutputFile()

