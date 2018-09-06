from math import *
from grapher import *

setViewBox(-3, -3.2, 3.4, 3.2)
openOutputFile("08unlabeledgraphs", 120)

eps=0.0001
twoeps = 2*eps
epssquare = eps*eps

def f(x):return (x+1)**2/(x*x+1.0)
def fx(t):
    global twoeps
    return (f(t+eps) - f(t-eps))/(twoeps)
def fxx(t): 
    global epssquare
    return (f(t+eps) - 2*f(t) + f(t-eps))/(epssquare)
def x(t): return t

axes([5,5])

linewidth(1.0)
plot(x, f, -3, 3)
plot(x, fx, -3, 3)
plot(x, fxx, -3, 3)

annotate([1, f(1)], [0,1], r"\bf C")
annotate([0.7, fx(0.7)], [1,1], r"\bf B")
annotate([0.7, fxx(0.7)], [2,1], r"\bf A")

closeOutputFile()
