
#!/usr/bin/python
# Time-stamp : Mon Nov 26 15:41:55 CST 2007 angenent

from  grapher  import *
from math import *

def x(z): return  cos(z)+0.2*sin(3*z)
def y(z): return  0.4*sin(z)+0.1*cos(2*z)

setViewBox(-1.5,-1.5,1.5,1.5)
openOutputFile("09slice",180)

Nt=300
dt=2*pi/Nt
tees=[i*dt for i in range(Nt+1)]


curve=[[x(t), y(t)] for t in tees]
polygonF(curve, fillcolor='white')

for i in range(61):
  t=2*i*pi/60
  line([x(t), y(t)], [x(t), y(t)+0.1])

curve=[[x(t), y(t)+0.1] for t in tees]
polygonF(curve, fillcolor='white')

closeOutputFile()


