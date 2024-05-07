from random import *

L = list(range(10))
# randomly generate answers
shuffle(L)
ans = L[0:4]

# print the answer
print(ans)

# the number of chances
C = 10
c = 0
while True :
    n = input("==> ")
    c = c + 1
    # compute the number of A's
    a = 0
    for i in range(len(ans)) :
        if ans[i] == int(n[i]) : a = a + 1 
    # compute the number of B's
    b = 0 
    for i in range(len(ans)) :
        for j in range(len(n)) :
            if i != j and ans[i] == int(n[j]) : b = b + 1
    # print the result
    S = " chance " if C-c <= 1 else " chances "
    print(a, " A ", b, " B ", " ---- ", C-c, S, "left", sep="")
    # close the game
    if c == C :
        print("Game Over!")
        break
    if a == 4 and b == 0 :
        print("Congratulations!")
        break
