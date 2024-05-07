p = "呆秀才吃長齋鬍鬚滿腮經書揭不開紙筆自己安排明年不請我自來"

k=0
p=p[len(p)-1::-1]
for i in range (1,8):
    q=p[k:k+i]
    print ("　"*(8-i),end ="")
    if i%2==1:
        q=q[len(q)-1::-1]
        for j in range (len(q)) :
            print (q[j],end="  ")
        print ()
        k=k+i
    else :
        for j in range (len(q)) :
            print (q[j],end="  ")
        print ()
        k=k+i
        
