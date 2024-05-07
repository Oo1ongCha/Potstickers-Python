S=100
T=999

for x in range (S,T+1):
    L=[]
    n=x
    while n>0:
        L.append(n%10)
        n=n//10
    k=len(L ) 
    E=0
    for a in L:
        E=E+a**k
    if E==x:
        print(x)
