while True :
    n=int(input("==> "))
    for a in range (n):
        for i in range (2*n-2):
            for b in range (n):
                for j in range (2*n-2):
                    if i==j or i+j==2*n-2:
                        print("*",end="")
                    else :
                        print(" ",end="")
            if i==0 or i==2*n-2:
                print ("*",end="")
                print()
            else:
                print()
    for k in range (n):
        print("*"," "*(2*n-4),end="")
    print("*")
       
            
