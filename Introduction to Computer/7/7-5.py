def check(n) :
    m = n
    c = d = 6
    while n > 0 :
        n = n // 10
        d = d * 10
    if d + m == 4*(10*m + c) :
        print(10*m + c)



for x in range(1, 1000000) :
    check(x)
