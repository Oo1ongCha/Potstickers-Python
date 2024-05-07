# M-1

k = 1
for i in range(9) :
    print(i+1, " x ", i+1, " x ", i+1, " = ", end="")
    k = k + 2*i
    for j in range(i+1) :
        print(k+2*j, "" if j ==i else " + ", sep="", end="")
    print() 




# M-2

while True :
    n = int(input("==> "))
    for i in range(1,n+1) :
        print("{0:>4}".format(i), end=" ")
        s = i
        for j in range(n-1) :
            if j % 2 == 0 :
                s = s + (2*(n-i)+1)
            else :
                s = s + (2*i-1)
            print("{0:>4}".format(s), end=" ")
        print()
            


# M-3

for i in range(10) :
    for j in range(10) :
        if i == 1 and j == 1 :
            print("＋", end="")
        if i == 0 and j == 0 :
            print("  x", end=" ")
        elif i == 1 :
            print("－－", end="")
        elif j == 1 :
            print("|", end=" ")
        elif i == 0 :
            print("{0:>3}".format(j), end=" ")
        elif j == 0 :
            print("{0:>3}".format(i), end=" ")
        else :
            print("{0:>3}".format(i*j), end=" ")
    print()



# M-4

for i in range(10) :
    S = 0
    k = 0
    for j in range(10) :
        v = (i+j) % 10
        S = S + v if k == 0 else S - v
        if j == 9 :
            s = "= "            
        elif v % 2 == 0 :
            s = "+ "
            k = 0
        else :
            s = "- "
            k = 1
        print(v, s, sep=" ", end="")
    print("{0:>2}".format(S))




# M-5

from math import *

d = 0.1
N = int((3.14*2)//d)
for n in range(21) :
    y = 1 - d*n 
    m = int(acos(y) // d)
    print(" "*m, "*", " "*(N-2*m), "*", sep="")



