__doc__ = """\
A set of extensions to the grapher module to accomodate three
dimensional drawings. 
"""
## import stuff 
print( "........Grapher3D" )
from grapher import *
print( "........Imported grapher" )
from numpy import *
print( "........Imported numpy" )

PMAT = matrix([[0.0,0.0], [1.0,0.0], [0.0,1.0]])


def rotatex(angle,pro): 
    c, s = cos(angle), sin(angle)
    return matrix([[1,0,0], [0,c, -s], [0, s, c]]) * pro
def rotatey(angle,pro): 
    c, s = cos(angle), sin(angle)
    return matrix([[c, 0, -s], [0,1,0], [s, 0, c]]) * pro
def rotatez(angle,pro): 
    c, s = cos(angle), sin(angle)
    return matrix([[c,-s,0], [s, c, 0], [0,0,1]]) * pro
def pr(q, debug=0): 
    """ Multiply the row matrix q with PMAT and return as list"""
    global PMAT
    if debug==1:
        print( "....pr\n", PMAT, q )
    qq = matrix(q)*PMAT
    return [qq[0,0], qq[0,1]]
def line3d(P,Q): 
    line(pr(matrix(P)), pr(matrix(Q)))
def shadowline3d(A, B,widths=[1,0.25], colors=['white','black']): 
    setrgbcolor(colors[0])
    linewidth(widths[0])
    line3d(A,B)
    setrgbcolor(colors[1])
    linewidth(widths[1])
    line3d(A,B)
def setProjection(pm): 
    global PMAT
    PMAT = pm
    print(  ".,.,.,.,projection matrix:\n", PMAT )
def resetProjection(): 
    global PMAT
    PMAT = matrix([[0,0], [1,0], [0,1]])
    print(  ".,.,.,.,projection matrix:\n", PMAT )
def theProjection(): 
    global PMAT
    return PMAT


