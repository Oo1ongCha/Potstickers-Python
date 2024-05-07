while True :
    n = int(input("==> "))
    for i in range (1,n+1):
        for j in range (1,n+1):
            print("{0} x {1} = {2:>2}".format(i, j, i*j), end="  ")
        print() 
