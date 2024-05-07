while True :
    n = int(input("==> ")) 
    for r in range(2,n+1) :
        m = r    
        print(m, "=", end=" ") 
        for i in range(2,m+1) :
            while m%i == 0 :
                m = m / i
                s = "x" if m > 1 else ""
                print(i, s, end=" ")                 
        print()
    print()
