def fun (x,n):
    y=0
    for i in range (n):
        y=y+int(x*(i+1))
    return y

print(fun (1,4))
