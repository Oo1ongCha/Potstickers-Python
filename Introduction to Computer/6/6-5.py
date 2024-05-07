while True:
    n=int(input("==>  "))
    print(n,"=",end=" ")

    for i in range (2,n+1):
        while n%i==0:
            n=n/i
            s="X" if n >1 else""
            print (i,s,end=" ")
    print ()
