#!/usr/bin/python2.7
# Time-stamp: Fri Sep 14 18:06:45 2012

from grapher import *

def x(t): return t
def fx(t): return t*(t+1)

def frame(frameno, scene, a, L, eps, delta, caption=""):
    openOutputFile("03epsAndDelta%03d"%(frameno),180, "eps")

    print "\nframno = %4d\nscene  = %4d\n\n"%(frameno, scene)

    polygonA( rect(Viewxmin(), Viewxmax(), Viewymin(), Viewymax()) )
    fxa = fx(a)

    # Bottom Layer
    if scene>2:
        setrgbcolor('magenta')
        linewidth(0)
        polygonF( rect(-0.04, 0.0, L-eps, L+eps) )
        linewidth(1)
        setrgbcolor('black')
    if scene>3:
        linewidth(3)
        setrgbcolor('cyan')
        polygonF( rect(a-delta, a+delta, -0.04, 0) )
        if scene>4:
            plot(x, fx, a-delta, a+delta)
            polygonF( rect(0, 0.04, fx(a-delta), fx(a+delta)) )
        linewidth(1)
        setrgbcolor('black')
    if scene>4:
        linewidth(0.5)
        polygonA([[a-delta, 0], [a-delta, fx(a-delta)], [0, fx(a-delta)]])
        polygonA([[a+delta, 0], [a+delta, fx(a+delta)], [0, fx(a+delta)]])
        linewidth(1)
    # Top Layer
    axes()
    plot(x, fx, -0.5, 2.0)
    if scene==1:
        xx=a-delta
        fxx=fx(xx)
        polygonA([[xx, 0], [xx, fxx], [0, fxx]])
        arrowhead([xx,fxx], [0,fxx], overshoot=-1)
    if scene<3:
        roundPoint([a,fxa], 0.03)
        roundPoint([a,0], 0.03)
        roundPoint([ a-delta, fx(a-delta) ], 0.03)
        roundPoint([a-delta,0], 0.03)
        roundPoint([0,fx(a-delta)], 0.03)
        roundPoint([0,L], 0.03)
        if abs(L-fxa)>0.1:
            roundPoint([0,fxa], 0.015)
    if scene>2:
        roundPoint([a,fxa], 0.015)
        roundPoint([a,0], 0.015)
        linewidth(0.5)
        setdash("[1 2] 0")
        line([Viewxmin(), L-eps], [Viewxmax(), L-eps])
        line([Viewxmin(), L+eps], [Viewxmax(), L+eps])
        setdash("[] 0")
    if scene>3:
        roundPoint([a-delta,0], 0.015)
        roundPoint([a+delta,0], 0.015)



    #annotations
    annotate([a, 0.0], [-2, -12], "$a$")
    annotate([x(0.95), fx(0.95)], [4,0], "$y=f(x)$")
    if scene<=2:
        annotate([a-delta, 0.0], [-2, -12], r"\textcolor{blue}{$x$}")
        annotate([0, fx(a-delta)], [-5, 0], makeboxr(r"\textcolor{blue}{$f(x)$}") )
    if scene==2:
        annotate([0.0, L], [-5, -2] ,r"\makebox[0pt][r]{$L$?}")
        if abs(L-fx(a))>0.1:
            annotate([0, fx(a)], [-5, -2], makeboxr(r"\tiny our first $L$"))
    if scene>2:
        annotate([0.0, L], [-5, 0] ,r"\makebox[0pt][r]{$L$}")
        annotate([Viewxmin(), L-eps], [3, 2], r"\makebox[0pt][l]{$L-\varepsilon$}")
        annotate([Viewxmin(), L+eps], [3, 2], r"\makebox[0pt][l]{$L+\varepsilon$}")
    if scene>3:
        annotate([a+delta, 0.0], [3, 3], "$a+\\delta$")
        annotate([a-delta, 0.0], [-24, 3], "$a-\\delta$")

    closeOutputFile('png', caption)
    return frameno+1

# main
setViewBox(-0.5,-0.5, 2.0,2.0)
a=x(0.7)
L=fx(0.7)
eps=0.4
delta=0.3
fno=1
#Scene 1: what is lim f(x) ?
dx=0.4
fno=frame(fno,1, a, L, eps, dx, r"""\color{red}
        Note the hole in the graph at $x=a$:\\
        \hfill $f(x)$ is undefined for $x=a$.""")
while dx>0.01:
    fno=frame(fno,1, a, L, eps, dx, r"""\color{blue}
        $f(x)$ is undefined for $x=a$\\
        \color{red}What is the limit of $f(x)$ as $x\to a$?""")
    dx*=0.85
#Scene 2: is it L?
fno=frame(fno,2, a, L, eps, delta, r"""\color{red}Is it $L$?""")
fno=frame(fno,2, a, L, eps, delta, r"""\raggedright\color{red}If it is, then we should be able to
        guarantee that $f(x)$ differs very little from $L$ if $x$ is close
        enough to $a$""")
#Scene 3, 4: show epsilon, then delta 
fno=frame(fno,3, a, L, eps, delta, r"""\textcolor{red}{$\varepsilon$ measures how close we want $f(x)$ to be to $L$}""")
fno=frame(fno,4, a, L, eps, delta, r"""\textcolor{red}{$\varepsilon$ measures how close we want $f(x)$ to be to $L$} \\
        \textcolor{blue}{$\delta$ measures how close  $x$ has to be to $a$  to achieve that.}""")
fno=frame(fno,5, a, L, eps, delta, r"""\color{red}This $\delta$ is too large.\\ Let's try a smaller $\delta$.""")
#Scene 5: show image of 0<|x-a|<delta for decreasing delta
fno=frame(fno,5, a, L, eps, delta/1.3, r"""\textcolor{red}{This $\delta$ is too big.}""")
fno=frame(fno,5, a, L, eps, delta/1.7, r"""\textcolor{red}{This $\delta$ is still too big.}""")
fno=frame(fno,5, a, L, eps, delta/2, r"""\textcolor{red}{This $\delta$ is small enough (barely).}""")
fno=frame(fno,5, a, L, eps, delta/3, r"""\textcolor{red}{This $\delta$ is small enough.}""")
fno=frame(fno,5, a, L, eps, delta/4, r"""\textcolor{red}{Any smaller $\delta$ is good enough.}""")
fno=frame(fno,5, a, L, eps, delta/6, r"""\textcolor{red}{Any smaller $\delta$ is good enough.}""")
fno=frame(fno,5, a, L, eps, delta/8, r"""\textcolor{red}{Any smaller $\delta$ is good enough.}""")
fno=frame(fno,5, a, L, eps, delta/12, r"""\textcolor{red}{Any smaller $\delta$ is good enough.}""")
# Repeat with the wrong L, but large epsilon
L=fx(a)-0.25
fno=frame(fno,2, a, L, eps, delta, r"""\textcolor{red}{Could some other number $L$ also be the limit?}""")
fno=frame(fno,3, a, L, eps, delta, r"""\textcolor{red}{To use the definition we pick an $\varepsilon$}""")
fno=frame(fno,4, a, L, eps, delta, r"""\textcolor{red}{To use the definition we pick an $\varepsilon$}\\
        \textcolor{blue}{and we look for a $\delta$.}""")
fno=frame(fno,5, a, L, eps, delta, r"""\textcolor{blue}{This $\delta$ is too large.}""")
fno=frame(fno,5, a, L, eps, delta/1.4, r"""\textcolor{blue}{This $\delta$ is too large.}""")
fno=frame(fno,5, a, L, eps, delta/2, r"""\textcolor{blue}{This $\delta$ is too large.}""")
fno=frame(fno,5, a, L, eps, delta/4, r"""\textcolor{blue}{This $\delta$ is too large.}""")
fno=frame(fno,5, a, L, eps, delta/6, r"""\textcolor{blue}{This $\delta$ is small enough.}""")
fno=frame(fno,5, a, L, eps, delta/8, r"""\textcolor{blue}{This $\delta$ is also small enough.}""")
fno=frame(fno,5, a, L, eps, delta/12, r"""\textcolor{blue}{And this $\delta$ is also small enough.}\\
        \textcolor{red}{Conclusion: the $L$ in this picture is also the limit of
        $f(x)$ as $x\to a$ ???}""")
# Repeat with the wrong L, but smaller epsilon
fno=frame(fno,2, a, L, eps, delta, r"""\color{red}A limit shouldn't be allowed to have two different values\\[1ex]
        \color{blue}There should be only one answer to the question\\[2ex]
        \color{magenta}\rule{3em}{0pt} ``How much is $\displaystyle\lim_{x\to a} f(x)$ ?'' """)
while eps>0.7*abs(fx(a) - L):
    fno=frame(fno,3, a, L, eps, delta, r"""\color{red}A limit shouldn't be allowed to have two different values.\\
            \color{blue}To see that this $L$ is not the limit we have to choose a smaller $\varepsilon$""")
    eps*=0.95
fno=frame(fno,4, a, L, eps, delta, r"""\color{red} With this $\varepsilon$ you can choose any $\delta$ you like""")
fno=frame(fno,5, a, L, eps, delta, r"""\color{red} With this $\varepsilon$ you can choose any $\delta$ you like
        \color{blue}but it will never be small enough""")
fno=frame(fno,5, a, L, eps, delta/2, r"""\color{red} With this $\varepsilon$ you can choose any $\delta$ you like
        but it will never be small enough\\
        \color{blue}to ensure that $L-\varepsilon <f(x) < L+\varepsilon$""")
fno=frame(fno,5, a, L, eps, delta/4, r"""\color{red} With this $\varepsilon$ you can choose any $\delta$ you like
        but it will never be small enough\\
        to ensure that $L-\varepsilon <f(x) < L+\varepsilon$\\
        \color{blue} if $a-\delta <x < a+\delta$.""")
fno=frame(fno,5, a, L, eps, delta/6, r"""\color{red} With this $\varepsilon$ you can choose any $\delta$ you like
        but it will never be small enough\\
        to ensure that $L-\varepsilon <f(x) < L+\varepsilon$\\
        \color{blue} if $a-\delta <x < a+\delta$.""")
fno=frame(fno,5, a, L, eps, delta/8, r"""\color{red} With this $\varepsilon$ you can choose any $\delta$ you like
        but it will never be small enough\\
        to ensure that $L-\varepsilon <f(x) < L+\varepsilon$\\
        \color{blue} if $a-\delta <x < a+\delta$.""")
fno=frame(fno,5, a, L, eps, delta/12, r"""\color{red} With this $\varepsilon$ you can choose any $\delta$ you like
        but it will never be small enough\\
        to ensure that $L-\varepsilon <f(x) < L+\varepsilon$\\
        \color{blue} if $a-\delta <x < a+\delta$.""")
fno=frame(fno,2, a, L, eps, delta, r"""\color{blue}Conclusion:\\ this $L$ is not the limit of $f(x)$ as $x\to a$. """)


