# Time-stamp: <2012-07-12 15:09:55 angenent>
from grapher import *

def x(t): return t
def fx(t): return cos(3*pi*t)/(1.0+t*t)
def rectangle(bl,tr, col):
    setrgbcolor(col)
    polygonF([
        bl,
        [bl[0], tr[1]],
        tr,
        [tr[0], bl[1]]
        ],
        col)
def figure(a, eps, title, caption="missing caption"):
    global xinf

    # Compute the graph of the function
    dx = float(xinf)/400
    xvals = [k*dx for k in range(401)]
    fvals = [fx(x) for x in xvals]
    graph = zip(xvals, fvals)
    aindex = int(a/dx)
    a=xvals[aindex]
    #find minimal and maximal values for x>a
    fmin = min(fvals[aindex:])
    minindex = fvals.index(fmin)
    xminf = xvals[minindex]
    if fmin>0:
        fmin=0.0
        xminf=xinf
    fmax = max(fvals[aindex:])
    maxindex = fvals.index(fmax)
    xmaxf = xvals[maxindex]

    setViewBox(-0.5,-1.0, xinf+0.25, 1.5)

    openOutputFile(title,360)

    #mark the epsilon target, delta source and its image
    linewidth(0)
    rectangle([-0.08, -eps], [0.0,  eps], 'magenta')
    #rectangle([a, -0.04], [xinf, 0.04], 'cyan')
    rectangle([0, fmin], [0.08, fmax], 'cyan')
    setrgbcolor('black')
    #draw the graphs
    linewidth(3)
    setrgbcolor('cyan')
    polygonA(graph[aindex:])
    linewidth(1.0)
    setrgbcolor('black')
    polygonA(graph)
    #axes
    axes()


    #Draw the horizontal epsilon lines
    linewidth(0.5)
    setdash("[1 2] 0")
    line([0.0, -eps], [Viewxmax(), -eps])
    line([0.0, +eps], [Viewxmax(), +eps])
    line([xvals[aindex], 0] , [ xvals[aindex], fvals[aindex] ])
    #Indicate where min and max are attained
    line([xvals[minindex], fmin], [0, fmin])
    line([xvals[maxindex], fmax], [0, fmax])
    setdash("[] 0")
    # Points of interest
    linewidth(1.0)
    roundPoint([a,0], 0.03)
    roundPoint([xvals[maxindex], fmax], 0.03)
    roundPoint([xvals[minindex], fmin], 0.03)
    #annotations
    annotate([a, 1], [0, 2], makeboxc("$A$"))
    linewidth(0.3)
    arrow([a,1], [a,0.1], 7, 2)
    annotate([0, eps], [-18, -3], r"$+\varepsilon$")
    annotate([0, -eps], [-18, -3],r"$-\varepsilon$")
    annotate([xinf-3, 1], [0,0], caption)
    #annotate([xvals[maxindex], fmax], [0,  6], "max") 
    #annotate([xvals[minindex], fmin], [0,-12], "min") 
    closeOutputFile()
def main():
    global xinf
    xinf=6.0
    okcaption = r"""%
\parbox{2in}{\centering This $A$ is large enough, because\\
 $f(x)$ is in the right range\\
for all $x\geq A$}""" 
    Atoosmallcaption = r"""%
\parbox{2in}{\centering Here $A$ is too small, because\\
 $f(x) > \varepsilon$ happens for some $x\geq A$}""" 
    figure(1.6, 0.33, "03ftozeroAok", makeboxl(okcaption))
    figure(0.7, 0.33, "03ftozeroAtoosmall", makeboxl(Atoosmallcaption))

main()

