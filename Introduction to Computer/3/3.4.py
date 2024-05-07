while True :
    n = int(input("==> "))
    for i in range(n) :
        print(" "*(n-1-i), end="")
        for j in range(n) :
            if i < n-1 :
                print("*"*(2*i+1) + " "*(2*(n-2-i)+1), end="")
            else :
                if j == 0 :
                    print("*"*(2*n-1), end="")
                else :
                    print("*"*(2*(n-1)), end="")
        print()
