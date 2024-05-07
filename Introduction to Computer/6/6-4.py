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
        E=10*E+a
    if E*x==280021:
        print(x)
