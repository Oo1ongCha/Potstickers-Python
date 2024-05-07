while True :
    n = int(input("==> "))
    m = n//2 + 1
    for i in range (n-2):
        for k in range (m) :
            if i==0 or i==n-3:
                print("*",end="")
            else :
                print ("|",end="")
            for j in range (n-2) :
                if i==j and i+j==n-3 :
                    print ("x",end="")
                elif i==j:
                    print ("\\",end="")
                elif i+j==n-3:
                    print ("/",end="")
                elif i+j<n-3 and i>j:
                    print ("|",end="")
                elif i+j>n-3 and i<j:
                    print ("|",end="")
                else :
                    print (" ",end="")
        print()
if i==0 or i==n-3:
        print("*",end="")
else :
        print ("|",end="")
