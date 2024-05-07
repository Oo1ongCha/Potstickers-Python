S=10
T=30
for a in range in (S,T+1):
    for b in range in (a+1,T+1):
        c =(a*a+b*b)**(0.5)
        if c>T:
            break
        if c-int(c)==0:
            print (a,b,int(c))
