while True :
    n = int(input("==> "))
    for a in range(n) :
        for i in range(n) :
            for b in range(2*n-1) :
                for j in range(n) :
                    if (a+b)%2 == 0 :
                        print(i+1, end=" ")
                    else :
                        print(" ", end=" ")
            print()
