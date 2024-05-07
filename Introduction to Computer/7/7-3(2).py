def fun (x,n):
    y=0
    for i in range (n):
        s=0
        for j in range(i+1):
            s=s+x*(10**j)
        y=y+s
    return y

print (fun(1,4))
