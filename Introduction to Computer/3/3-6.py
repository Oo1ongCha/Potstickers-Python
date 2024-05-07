while True :
    n = int(input("==> "))
    m=n//2
    for i in range (n) :
        for j in range (n):
            if i==j or i+j==n-1 :
                print("x",end="")
            elif j>i and i+j< n-1 :
                print((m-i),end="")
            elif j<i and i+j>n-1 :
                print((i-m),end ="")
            elif j<i and i+j<n-1 :
                print((m-j),end="")
            elif j>i and i+j>n-1 :
                print((j-m),end="")
        print ()
            
