__doc__ = """\
---------------------------------------------------
........Python routines in aid of creating EPS drawings
........If epstopdf (ghostscript) is installed
........PDF figures are also produced.
........Also, a LaTeX picture file with annotations is
........created.

<<<<<<<<<<<<<<<grapher.py>>>>>>>>>>>>>>>

........2006,2007 Joel Robbin
........2007--09 Sigurd Angenent
---------------------------------------------------
"""
import os, string, sys
from math import *
def setViewBox(xmin, ymin, xmax, ymax): 
    global ViewBox
    ViewBox=[xmin, ymin, xmax, ymax]
    _epsX_ = 0.0001*(xmax-xmin)
    _epsY_ = 0.0001*(ymax-ymin)
def Viewxmin(): 
    global ViewBox
    return ViewBox[0]
def Viewxmax(): 
    global ViewBox
    return ViewBox[2]
def Viewymin(): 
    global ViewBox
    return ViewBox[1]
def Viewymax(): 
    global ViewBox
    return ViewBox[3]
def openOutputFile(name, width, graphics_extension="eps"): 
    # And inititialize
    r"""open two output files:
      one .eps file and one .tex file
      The .eps file contains the drawings
      The .tex file contains a {picture} environment which can be
      \included in any latex document in the parent directory.
      It provides the figure with annotations.
      One must set ViewBox before calling openOutputFile.
      BoundingBox will be computed by rescaling the ViewBox
      to width (points).
      Including a one point margin around the ViewBox into the BoundingBox.
    """
    global outfile, texfile, filename
    global scale,hshift,vshift,BoundingBox,ViewBox
    print """........opening output file  |%s|"""%(name)
    fullcwd = os.getcwd()
    cwd=fullcwd.split("\\")   #  USE '\\' for WINDOWS!!!!
    cwd=cwd[-1]
    print """........current working directory is
    |%s| from |%s|"""%(cwd,fullcwd)

    BoundingBox = [0,0,0,0]
    BoundingBox[2]=width
    scale = (width-2)/(1.0*(ViewBox[2]-ViewBox[0]))
    BoundingBox[3]=scale*(ViewBox[3]-ViewBox[1])+2
    #
    hshift = BoundingBox[0]-scale* ViewBox[0]+1
    vshift = BoundingBox[1]-scale* ViewBox[1]+1
    print """\
    scale = %0.2f hshift = %0.2f vshift = %0.2f
    Boundingbox = [%0.2f, %0.2f, %0.2f, %0.2f]"""%(
        scale, hshift, vshift,
        BoundingBox[0],BoundingBox[1],BoundingBox[2],BoundingBox[3])
    filename=name
    outfile=open(filename+".eps","w")
    topMatter =  "%!PS-Adobe-2.0 EPSF-2.0\n"
    topMatter += "%%Title: "+filename+".eps\n"
    topMatter += "%%BoundingBox: "
    for b in BoundingBox: topMatter += " "+str(b)
    #
    outfile.write(topMatter + "\n\n")
    #  Let all lines have round caps and joins by default
    setlinejoin(1)
    setlinecap(1)
    #  Prepare the latex file
    texfile=open(filename+".tex","w")
    topMatter = r"""%%
\begin{picture} (%6f,%6f)(0,0)
\put(0.0, 0.0){\includegraphics{%s/%s.eps}}
"""%(BoundingBox[2], BoundingBox[3], cwd, filename)
    #The above lines go into the tex file.  Even though windows uses the
    #backslash, it seems tex always uses a slash to separate directories and files
    texfile.write(topMatter)
def closeOutputFile(): 
    global outfile, texfile, filename
    outfile.write("showpage\n")
    print "........closing %s.eps"%(filename)
    outfile.close()
    texfile.write("\\end{picture}\n")
    print "........closing %s.tex"%(filename)
    texfile.close()
    print "........making %s.pdf"%(filename)
    os.system("epstopdf %s.eps"%(filename))
    print "........done"
def line(p,q): 
    global scale,hshift,scale,vshift
    p1=scale*p[0] + hshift
    p2=scale*p[1] + vshift
    q1=scale*q[0] + hshift
    q2=scale*q[1] + vshift
    outfile.write("%6.2f %6.2f moveto\n" % (p1,p2))
    outfile.write("%6.2f %6.2f lineto\n" % (q1,q2))
    outfile.write("stroke\n")
def arrowhead(A, B, len=10, wid=3, overshoot=1.0): 
    """Draw an arrow of length len(points) and width wid(points).
    Advance the arrow by overshoot(points).
    The direction of the arrowhead is from A to B."""
    outfile.write("%%%%Arrow head with length %6.2f and width %6.2f points\n"
                  %(len, wid))
    aa=complex(A[0], A[1])
    bb=complex(B[0], B[1])
    direction=(bb-aa)/abs(bb-aa)
    arrow=[0+0j,    # set up the basic arrow
           complex(-len, -wid),
           complex(-0.7*len, 0), 
           complex(-len, wid),
           0+0j]
    arrow = [bb+direction*(p+overshoot)/scale for p in arrow] 
    arrow = [[p.real, p.imag] for p in arrow]
    __polygon__(arrow, " gsave fill grestore stroke")
def arrow(A, B, len=10, wid=3, overshoot=1.0): 
    line(A, B)
    arrowhead(A, B, len, wid, overshoot)
def movepoint(p, offset): 
    p0=p[0]+offset[0]/scale
    p1=p[1]+offset[1]/scale
    return [p0,p1]
def x_axis(arrowsize=10): 
    A=[ViewBox[0], 0.0]
    B=[ViewBox[2], 0.0]
    line(A, B)
    arrowhead(A, B, arrowsize, 0.3*arrowsize, overshoot=-0.1)
def y_axis(arrowsize=10): 
    A=[0.0, ViewBox[1]]
    B=[0.0, ViewBox[3]]
    line(A, B)
    arrowhead(A, B, arrowsize, 0.3*arrowsize, overshoot=-0.1)
def axes(arrowsize=[10,10]): 
    linewidth(0.5)
    x_axis(arrowsize[0])
    y_axis(arrowsize[1])
    linewidth(1)
def grid(XMIN, XMAX, DX, YMIN, YMAX, DY): 
    x=XMIN
    while (x < XMAX+_epsX_):
      x+=DX
      line([x, YMIN], [x, YMAX])
    y=YMIN
    while (y < YMAX+_epsY_):
      y+=DY
      line([XMIN, y], [XMAX, y])
def inBoundingBox(x,y): 
    global BoundingBox
    return BoundingBox[0]<x and x<BoundingBox[2]  \
            and BoundingBox[1]<y and y<BoundingBox[3] 
def __polygon__(P,s): 
    # don't call directly
    x2=(scale*P[0][0]+hshift)
    y2=(scale*P[0][1]+vshift)
    inBB2 = inBoundingBox(x2,y2)
    if inBB2:
        outfile.write("%6.2f %6.2f moveto\n" % (x2,y2))
    for point in P[1:]:
        x1,y1,inBB1=x2,y2,inBB2
        x2=(scale*point[0]+hshift)
        y2=(scale*point[1]+vshift)
        inBB2=inBoundingBox(x2,y2)
        if inBB1:
            if inBB2:
                outfile.write("%6.2f %6.2f lineto\n" % (x2,y2))
            else:
                outfile.write("stroke\n")                
                print "%s %6.2f %6.2f %6.2f%6.2f"%(\
                        "__polygon__ going out of bounds:",x1,y1,x2,y2)
        else:
            if inBB2:
                print "%s %6.2f %6.2f %6.2f%6.2f"%(\
                        "__polygon__ back in bounds: ",x1,y1,x2,y2)
                outfile.write("%6.2f %6.2f moveto\n" % (x2,y2))
    if inBB2:
        outfile.write(s+"\n")
def polygonA(P): 
    # polygonal arc
    __polygon__(P,"stroke")
def polygonC(P): 
    # closed polygon
    __polygon__(P,"closepath stroke")
def polygonF(P, fillcolor=0): 
    # filled polygon
    if fillcolor==0:
        __polygon__(P, "fill")
    else:
        __polygon__(P,"gsave \n")
        setrgbcolor(fillcolor)
        outfile.write("fill grestore stroke \n") 
def plot(x, y, tmin, tmax): 
    global scale, hshift, scale, vshift, outfile, ViewBox
    print "plot parameter range %lf...%lf"%(tmin, tmax)
    dt=(1.0*(tmax-tmin))/500
    times=[tmin+k*dt for k in range(501)]
    poly = [[x(t), y(t)] for t in times]
    __polygon__(poly, " stroke")
def plotfun(f):  
  plot((lambda t:t), f, Viewxmin(), Viewxmax())
def arc(center, radius, angle, op="stroke"): 
    """Plots an arc using the postscript arc command
    angle should be a pair [alpha, omega] where alpha is
    the beginning and omega is the final angle of the arc.
    Angles should be in degrees.
    """
    global scale,hshift,scale,vshift
    cx=(scale*center[0]+hshift)
    cy=(scale*center[1]+vshift)
    r = scale*radius
    outfile.write("newpath\n")
    outfile.write("%6.2f %6.2f moveto\n"%(
        cx+r*cos((pi/180)*angle[0]),
        cy+r*sin((pi/180)*angle[0])))
    outfile.write("%6.2f %6.2f %6.2f %6.2f %6.2f arc\n"\
                      %(cx, cy, r, angle[0], angle[1]))
    outfile.write(op+"\n")
def rgbcolor(colorname): 
    __rgbcolors__ = {'white'    : [255,255,255],
                     'black'    : [0,0,0],
                     'gray'     : [128,128,128],
                     'darkGray' : [64,64,64],
                     'lightGray': [192,192,192],
                     'red'      : [255,0,0],
                     'green'    : [0,255,0],
                     'blue'     : [0,0,255],
                     'yellow'   : [255,255,0],
                     'magenta'  : [255,0,255],
                     'cyan'     : [0,255,255],
                     'orange'   : [255,200,0],
                     'pink'     : [255,175,175],
                     'cayenne'  : [64, 0, 0],
                     'ocean'    : [0, 64, 128],
                     'teal'     : [0,128, 128],
                     'aqua'     : [0,128, 255],
                     'midnight' : [0,  0, 128],
                     'eggplant' : [64, 0, 128],
                     'tangerine': [255,128, 0],
                     'plum'     : [128,0, 128]}
    return __rgbcolors__[colorname]
def setrgbcolor(rgb): 
    """set rgbcolor(rgb)  rgb is sring or [256,256,256] """
    if isinstance(rgb, str):
        rgb = rgbcolor(rgb)
    outfile.write("%3f %3f %3f setrgbcolor\n"\
                  % (rgb[0]/256.0,rgb[1]/256.0,rgb[2]/256.0))
def setlinecap(num): 
    outfile.write("%3d setlinecap\n" % (num))
def setlinejoin(num): 
    outfile.write("%3d setlinejoin\n" % (num))
def setdash(dash_string): 
    outfile.write(dash_string + " setdash\n")
def linewidth(w): 
    outfile.write("%6.2f"%(1.0*w)+" setlinewidth\n")
def roundPoint(center, radius=0.02, annotation="", fillcolor='white'): 
    """Plots a filled round circle using the postscript arc command
    and includes annotation in the latex file"""
    global scale,hshift,scale,vshift
    cx=(scale*center[0]+hshift)
    cy=(scale*center[1]+vshift)
    r = scale*radius
    outfile.write("newpath\n")
    outfile.write("%6.2f %6.2f moveto\n"%(cx+r, cy))
    outfile.write("%6.2f %6.2f %6.2f 0 360 arc\n"%(cx, cy, r))
    outfile.write("gsave \n")
    setrgbcolor(fillcolor)
    outfile.write("fill grestore \n")
    outfile.write("stroke\n")
    if len(annotation)>0:
        texcommand = "\\put(%6.2f, %6.2f)"%(cx, cy-12.0)
        texcommand += "{"+annotation+"}\n"
        texfile.write(texcommand)

def annotate(location, offset, annotation): 
    """includes annotation in the latex file
       The annotation will be placed at location (in viewbox coordinates)
       with an offset (in Bounding Box coordinates)
       """
    global scale,hshift,scale,vshift
    x=(scale*location[0]+hshift)+offset[0]
    y=(scale*location[1]+vshift)+offset[1]
    texcommand = "    \\put(%6.2f, %6.2f)"%(x, y)
    texcommand += "{\\sffamily\\itshape "+annotation+"}"
    #print texcommand
    texfile.write(texcommand+"\n")
def makeboxr(tex): 
    return r"\makebox[0pt][r]{%s}"%(tex)
def makeboxl(tex): 
    return r"\makebox[0pt][l]{%s}"%(tex)
def makeboxc(tex): 
    return r"\makebox[0pt][c]{%s}"%(tex)
def rotatebox(angle, tex): 
    return r"\rotatebox{%lf}{%s}"%(angle, tex)
def PStext(location, offset, thetext, font="Helvetica", size=9): 
    global scale,hshift,scale,vshift
    p1=(scale*location[0]+hshift)+offset[0]
    p2=(scale*location[1]+vshift)+offset[1]
    outfile.write("/%s findfont %d scalefont setfont \n"%(font, size))
    outfile.write("%6.2f %6.2f moveto\n" % (p1,p2))
    outfile.write("(%s) show\n"%(thetext))
    #topMatter += "/regfont {/Times-Roman findfont 10 scalefont setfont } def\n"
    #topMatter += "/smlfont {/Times-Roman findfont 7  scalefont setfont } def\n"


