#!/usr/bin/python
# Time-stamp: <2007-08-20 17:26:36 sigurdangenent>

from grapher import *

def x(t): return t
def fx(t): return t*(t+1)

a=x(0.7)
L=fx(0.7)
eps=0.4
delta=1.0
while (fx(a+delta)>L+eps) or (fx(a-delta)<L-eps):
    delta=delta/2.0
    print delta

setViewBox(-0.5,-0.5, 2.0,2.0)

openOutputFile("03epsAndNoDelta",180)

#mark the epsilon target
setrgbcolor('magenta')
polygonF([[0, L-eps],
        [-0.04, L-eps],
        [-0.04, L+eps],
        [0.0,  L+eps],
        [0.0, L-eps]], 'magenta')
setrgbcolor('black')
#axes
axes()

# graph of the function
plot(x, fx, -0.5,  2.0)

polygonA([[a, 0], [a, L], [0, L]])
arrowhead([a,L], [0,L], overshoot=-1)

linewidth(0.5)
setdash("[1 2] 0")
line([Viewxmin(), L-eps], [Viewxmax(), L-eps])
line([Viewxmin(), L+eps], [Viewxmax(), L+eps])

#line([x(0.3), 0.0], [x(0.3), fx(0.3)])
#line([x(0.3), fx(0.3)], [0.0, fx(0.3)])

setdash("[] 0")

rangearrows = 2*a
line([rangearrows, L+0.5*eps], [rangearrows, L+eps])
arrowhead([rangearrows, L+0.4*eps], [rangearrows, L+eps], 6,2, overshoot=-1)
line([rangearrows, L-0.5*eps], [rangearrows, L-eps])
arrowhead([rangearrows, L-0.2*eps], [rangearrows, L-eps], 6,2, overshoot=-1)

roundPoint([a,0], 0.015)
roundPoint([a,L], 0.015)
arrowhead([a,0], [a, L/2])


#annotations
annotate([Viewxmin(), L-eps], [-3, 0], r"\makebox[0pt][r]{$L-\varepsilon$}")
annotate([Viewxmin(), L+eps], [-3, 0], r"\makebox[0pt][r]{$L+\varepsilon$}")
annotate([0.0, L], [-5, 0] ,r"\makebox[0pt][r]{$L$}")
annotate([x(0.95), fx(0.95)], [4,0], "$y=f(x)$")
annotate([a, 0.0], [-2, -12], "$a$")
#annotate([0.3, 0.0], [-2, -12], "$x$")
#annotate([0.0, fx(0.3)], [3, 5] ,"$f(x)$")
annotate([a, L], [5,0], r"""\
How close must $x$ be to $a$ for $f(x)$ to end up in this range?
""")

closeOutputFile()


