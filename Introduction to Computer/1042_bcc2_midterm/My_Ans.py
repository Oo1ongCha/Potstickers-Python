#M1
for i in range (1,10):
        print(i,"X",i,"X",i,"=",(i-1)*(i)+1,sep=" ",end="")
        for j in range (i-1):
            if (i-1)*(i)+1+2*(j+1)>0:
                print(" + ",(i-1)*(i)+1+2*(j+1),end="")
            else:
                print(" ",end="")
        print()
        
#M2
while True:
    n=int(input("==>  "))
    for a in range(n):
        for b in range(n):
            if b%2==0:
                print ("{0:>3}".format(b*n+a+1),end=" ")
            else :
                print ("{0:>3}".format(b*n+n-a),end=" ")
     
        print()
        
#M3
for i in range (10):
    for j in range (9):
        if j==0 and i==0:
            print("  X  ｜",end="")
        elif j==0 and i == 1:
            print("─","─"," ＋",end="",sep="")
        elif i==0:
            print("{0:>3}".format(j+1),end=" ")
        elif i==1:
            print("─"*2,end="")
        else:
            if j==0:
                print(" ",i," ｜",end="")
            else:
                print ("{0:>3}".format(i*(j+1)),end=" ")
    print()

#M4
p=[0,1,2,3,4,5,6,7,8,9]
q=["+","-"]
for a in range(9):
    for b in range(9):
        if b%2==0:
            l=(a+b)%10
            print ("{0:>2}".format(p[l]),end=" ")
        else :
            k=(a+b)%2
            if a%4==1:
                if k-1==0:
                    print(q[1],end=" ")
                else:
                    print(q[2],end=" ")
            else:
                if k-1==0:
                    print(q[2],end=" ")
                else:
                    print(q[1],end=" ")
    if a %2==0:
        print ("=","{0:>2}".format(5+2*a),end=" ")
    else:
        print ("=","{0:>2}".format(5),end=" ")
    print()


#M5
for i in range (0,2*3.14,0.1):
    for j in range (1,-1.1,-0.1):
        if cos(i)==j :
            print("*",end="")
        else:
            print(" ",end="")
