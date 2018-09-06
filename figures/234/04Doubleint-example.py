from grapher3d import *
#  Set rotation matrix {{{1
setProjection (matrix( [[0,0], [1,0], [0,1]] ))
setProjection (rotatey(pi/5, theProjection ()))
setProjection (rotatez(-1.9, theProjection ()))
print( PMAT )

def fun(x, y): return x*x+y*y #{{{1

def xstripe(x): #{{{1
    dy = 1.0/50
    pol = [[x, k*dy, fun(x, k*dy)] for k in range(51)]
    pol = [pr(matrix(pt)) for pt in pol]
    polygonA(pol)

def ystripe(y): #{{{1
    dx = 1.0/50
    pol = [[k*dx, y, fun(k*dx, y)] for k in range(51)]
    pol = [pr(matrix(pt)) for pt in pol]
    polygonA(pol)

setViewBox(-0.5,-0.2,1.3,2.5) #{{{1
openOutputFile("04Doubleint-example", 200)


for x in (0.0, 1.0):
    xstripe(x)
for y in (0.0, 1.0):
    ystripe(y)

linewidth(0.4)
xlist = [k*0.05 for k in range(1,20)]
for t in xlist:
    xstripe(t)
    ystripe(t)

for k in range(41):
    t=0.025*k
    line3d([0,t,0], [0, t, fun(0,t)])
    line3d([t,0,0], [t, 0, fun(t,0)])
linewidth(0.2)
setdash("[2 2] 0")
line3d([0,0,0], [0,1,0])
line3d([0,1,0], [1,1,0])
line3d([1,1,0], [1,0,0])
line3d([1,0,0], [0,0,0])
line3d([1,1,0], [1, 1, fun(1,1)])

# The axes. {{{1
setdash("[] 0")
linewidth(1)
line3d([-0.3,0,0], [1.2,0,0])
line3d([0,-0.3,0], [0,1.2,0])
line3d([0,0,-0.2], [0,0,0.5])
shadowline3d([0,0,0.05], [0,0,2.4], [2.5, 1])
# The surrounding block {{{1
linewidth(0.5)
top = fun(1, 1)
line3d([1,0,fun(1,0)], [1,0, top])
line3d([1,1, top], [1,0, top])
line3d([1,1, top], [0,1, top])
line3d([0,1, fun(0,1)], [0,1, top])
line3d([0,0, top], [0,1, top])
line3d([0,0, top], [1,0, top])
# Annotation {{{1
PStext (pr([1.2,0,0]), [0, 3], "x", 'Palatino-Italic', 12)
PStext (pr([0,1.2,0]), [-5, 0], "y", 'Palatino-Italic', 12)
PStext (pr([0,0,2.4]), [3, 0], "z", 'Palatino-Italic', 12)

closeOutputFile()
