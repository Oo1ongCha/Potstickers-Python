def Pascal(n) :
    L = []
    for i in range(n) :
        L.append(1)
        for j in range(len(L)-2, 0, -1) :
            L[j] = L[j-1] + L[j]
        print("   "*(n-i), end="")
        for j in range(len(L)) :
            print("{0:>3}".format(L[j]), end="   ")
        print()
        
Pascal(10)
