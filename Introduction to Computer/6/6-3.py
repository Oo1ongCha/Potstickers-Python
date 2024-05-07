S=1
T=999

for x in range (S,T+1):
    L=[]
    n=x
    while n>0:
        L.append(n%10)
        n=n//10
    k=len(L) 

    E=x*x%10**k
    
    if E==x:
        print(x)
