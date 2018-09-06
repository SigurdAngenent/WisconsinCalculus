
#!/usr/bin/python2.5
# Time-stamp: Mon Jun  2 10:06:41 CDT 2008 angenent

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
delta*=2

setViewBox(-0.5,-0.5, 2.0,2.0)

openOutputFile("03epsAndDeltaTooBig",180)

#mark the epsilon target, delta source and its image
setrgbcolor('magenta')
linewidth(0)
polygonF([[0, L-eps],
        [-0.04, L-eps],
        [-0.04, L+eps],
        [0.0,  L+eps],
        [0.0, L-eps]], 'magenta')
setrgbcolor('cyan')
polygonF([[a-delta, 0],
    [a+delta, 0],
    [a+delta, -0.04],
    [a-delta, -0.04],
    [a-delta,0]], 'cyan')
polygonF([[0, fx(a-delta)],
        [0.04, fx(a-delta)],
        [0.04, fx(a+delta)],
        [0.0,  fx(a+delta)],
        [0.0, fx(a-delta)]], 'cyan')
setrgbcolor('black')
#axes
axes()

# graph of the function
linewidth(5)
setrgbcolor('cyan')
plot(x, fx, a-delta, a+delta)
linewidth(1.0)
setrgbcolor('black')
plot(x, fx, -0.5, 2.0)


polygonA([[a, 0], [a, L], [0, L]])
arrowhead([a,L], [0,L], overshoot=-1)
linewidth(0.5)
setdash("[1 2] 0")
line([Viewxmin(), L-eps], [Viewxmax(), L-eps])
line([Viewxmin(), L+eps], [Viewxmax(), L+eps])
polygonA([[a-delta, 0], [a-delta, fx(a-delta)], [0, fx(a-delta)]])
polygonA([[a+delta, 0], [a+delta, fx(a+delta)], [0, fx(a+delta)]])
setdash("[] 0")

roundPoint([a,L], 0.015)
roundPoint([a,0], 0.015)
roundPoint([a-delta,0], 0.015)
roundPoint([a+delta,0], 0.015)

#annotations
annotate([Viewxmin(), L-eps], [-3, 0], r"\makebox[0pt][r]{$L-\varepsilon$}")
annotate([Viewxmin(), L+eps], [-3, 0], r"\makebox[0pt][r]{$L+\varepsilon$}")
annotate([0.0, L], [-5, 0] ,r"\makebox[0pt][r]{$L$}")
annotate([x(0.95), fx(0.95)], [4,0], "$y=f(x)$")

annotate([a+delta, 0.0], [3, 3], "$a+\\delta$")
annotate([a-delta, 0.0], [-24, 3], "$a-\\delta$")
annotate([a, 0.0], [-2, -12], "$a$")

line([a+delta/2, -0.02], [a+2*delta, (L-eps)/2])
annotate([a+2*delta, (L-eps)/2], [3,0], r"""\begin{minipage}{240pt}
        For some $x$ in this interval $f(x)$ is not between
        $L-\varepsilon$ and $L+\varepsilon$. Therefore the $\delta$ in this
        picture is too big for the given $\varepsilon$.  You need a smaller
        $\delta$.
        \end{minipage}""")
closeOutputFile()


