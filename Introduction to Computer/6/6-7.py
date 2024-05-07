while True :
    n = int(input("==> ")) 
    for r in range(2,n+1) :
        m = r    
        print(m, "=", end=" ")
        k=1
        c=0
        for i in range(2,m+1) :
            while m%i == 0 :
                m = m / i
                s = "x" if m > 1 else ""
                print(i, s, end=" ")
                if k!=i:
                    k=i
                    c=c+1
        print("[", c, "]", sep="")
    print()
