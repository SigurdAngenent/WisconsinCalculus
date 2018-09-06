from grapher3d import *

def helix(t): # {{{1
    return (cos(t), sin(t), t/pi)
###  set projection matrix     {{{1
print( theProjection() )
setProjection(rotatey(pi/6, theProjection()))
setProjection(rotatez(pi/6, theProjection()))
print( theProjection() )

print( pr([1,0,0],1) )

setViewBox(-2, -1.8, 2, 1.3) # {{{1
openOutputFile("04saddle-sliced", 400)
polygonA( rect(Viewxmin()+0.02,
    Viewxmax()-0.02,
    Viewymin()+0.02,
    Viewymax()-0.02 ))
## The axes {{{1
line3d([0,-1.4,0], [0,1.4,0])
line3d([-1.4,0,0], [1.9,0,0])
line3d([0,0,-2.0], [0,0,1.0])
## Draw slices {{{1
N=4
dx = 1.0/N
for a in range(-N, N+1):
    A= [a*dx, -1.0,  a*dx]
    B= [a*dx,  1.0, -a*dx]
    C= [ 1.0, -a*dx,  a*dx]
    D= [-1.0, -a*dx, -a*dx]
    #setrgbcolor('white')
    #polygonF( [A,B,C,D, A] )
    #setrgbcolor('chartreuse')
    shadowline3d( A, B , [4,1], ['white', 'red'])
    if a<N-2:
        shadowline3d( C, D , [4,0.3], ['white', 'navyblue'])

closeOutputFile()


