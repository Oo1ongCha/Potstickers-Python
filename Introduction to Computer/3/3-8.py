while True :
    n = int(input("==> "))
    m = n//2 + 1
    for i in range (n):
        for k in range (m) :
            for j in range (n) :
                if i==j and i+j==n-1 :
                    print ("x",end="")
                elif i==j:
                    print ("\\",end="")
                elif i+j==n-1:
                    print ("/",end="")
                elif i+j<n-1 and i>j:
                    print ("|",end="")
                elif i+j>n-1 and i<j:
                    print ("|",end="")
                else :
                    print (" ",end="")
        print()
