from math import *
roottwo = (1.0, 1.4, 1.41, 1.414, 1.4142, 1.41421, 1.414213, 1.4142135)

for x in roottwo:
    print "%14.10f &  %14.12f  \\\\"%(x, 2**x)
