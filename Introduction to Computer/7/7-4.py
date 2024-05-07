def fibonacci(k):
    F = [0] * k
    F[1] = 1
    for n in range(2, k) :
        F[n] = F[n-1] + F[n-2]
    return F

print(fibonacci(20))
