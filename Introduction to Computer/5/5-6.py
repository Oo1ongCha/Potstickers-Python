p="春眠不覺曉處處聞啼鳥夜來風雨聲花落知多少"
while True :
    R=int(input("==> "))
    N=len(p)
    C=N//R+(1 if N%R else 0)

    for i in range (R):
        for j in range (C-1,-1,-1):
            k=R*j+i
            print (p[k] if k<N else "  ",end =" ")
        print()
    print()
    
