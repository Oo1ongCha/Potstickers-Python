while True:
    n=int(input("==>  "))
    m=n
    L=[]
    for i in range (2,n+1):
        while n%i==0:
            L.append(str(i))
            n=n/i
    S=" X ".join(L)
    print(m,"=",S)
