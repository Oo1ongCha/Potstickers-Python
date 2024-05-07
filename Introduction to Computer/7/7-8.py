def findAllPrimes(n):
    Prime = [2]
    for x in range(3, n+1) :
        isprime = 1
        for p in range(2, x) :
            if x % p == 0 :
                isprime = 0
                break
        if isprime : Prime.append(x)
    return Prime
                
    
n = 100
Prime = findAllPrimes(n)

for i in range(len(Prime)) :
    for j in range(i+1, len(Prime)) :
        y0, y1 = Prime[i], Prime[j]
        d = y1 - y0
        yn = y1 + d
        s = []
        while yn < n and (yn in Prime):
            s.append(yn)
            yn = yn + d
        if s :
            print([y0, y1] + s)
