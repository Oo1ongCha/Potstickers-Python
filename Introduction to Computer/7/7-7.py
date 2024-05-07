def check_prime(n) :
    if n == 2 : return True 
    for i in range(2,n) :
        if n % i == 0 :
            return False        
    return True


def reverse_number(n) :
    L = []
    while n > 0 :
        L.append(n % 10)
        n = n // 10
    s = 0
    for i in range(len(L)) :
        s = s + L[i]*(10**(len(L)-i-1))
    return s


c = 0
for x in range(1, 201) :
    a = check_prime(x)
    if a :
        b = check_prime(reverse_number(x))
    else :
        b = False
    if a and b :
        c = c + 1
        print(x)
print("==>", c, "primes satisfying the condition")
