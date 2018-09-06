from math import *

dxlist=[0.1,
        0.01,
        0.001,
        0.0001,
        0.00001,
        0.000001,
        0.0000001,
        0.00000001,
        0.000000001,
        0.0000000001,
        0.00000000001,
        0.000000000001]

correctanswer=2*log(2)

print "\n\n\n"
print "%15s %15s %10s\n"%(" dx ", "approximation", "error" )
for dx in dxlist:
    approximation = (2**(1+dx)-2)/dx
    error = approximation - correctanswer
    print "%15.12f %15.12f %15.12f"%(dx, approximation, error)

print "done"
