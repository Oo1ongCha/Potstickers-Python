while True :
    n = int(input("==> ")) 
    w = 0 
    for r in range(2,n+1) :
        m = r
        print(m, "=", end=" ") 
        k = 1 
        c = 0 
        z = 0 
        for i in range(2,m+1) :
            while m%i == 0 :
                m = m / i 
                z = z + 1
                s = "x" if m > 1 else ""
                print(i, s, end=" ")
                if k != i : 
                    k = i 
                    c = c + 1
        print("[", c, "]", sep="") 
        if z == 1 : w = w + 1
    print("number of primes: ", w) 
