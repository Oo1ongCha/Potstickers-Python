while True :
    n=int(input("==> "))
    m=n//2
    for a in range (n):
        for i in range (n):
            for b in range (2*n-1):
                for j in range (n):
                    if (a+b)%2==0:
                        if i==j==m:
                            print("x",end="")
                        elif i==j:
                            print("\\",end="")
                        elif i+j==n-1:
                            print("/",end="")
                        else :
                            print(" ",end="")
                    else:
                        print (" ",end="")
            print()
