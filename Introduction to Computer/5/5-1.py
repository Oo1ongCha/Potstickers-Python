p = "呆秀才吃長齋鬍鬚滿腮經書揭不開紙筆自己安排明年不請我自來"

k=0
for i in range (1,8):
    q=p[k:k+i]
    s=q[len(q)-1::-1]
    print ("　"*(8-i),end ="")
        for j in range (len(q)) :
        if i%2==0:
            print (s[j],end="  ")
        else:
            print (q[j],end="  ")
    print ()
    k=k+i
        
