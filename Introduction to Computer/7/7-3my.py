def fun (x,n):
    y=0
    for i in range(n):
        y=y+x*(n-i)*10**i
    return y
print (fun(1,4))
