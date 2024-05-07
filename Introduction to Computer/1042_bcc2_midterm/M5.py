from math import *

d = 0.1
N = int((3.14*2)//d)
for n in range(21) :
    y = 1 - d*n 
    m = int(acos(y) // d)
    print(" "*m, "*", " "*(N-2*m), "*", sep="")
