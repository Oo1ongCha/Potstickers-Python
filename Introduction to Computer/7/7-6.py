def fraction(a, b) :    
    print(a, "/", b, "= ", end="")
    while a > 0 :        
        if b % a == 0 :
            k = b // a - 1
            a = 0            
        else :
            k = b // a        
            a = a*(k+1) - b
            b = b*(k+1)
        print(1, "/", k+1, "" if a == 0 else "+ ", end="")
    print()
        

fraction(3, 7)
fraction(4, 9)
fraction(7, 15)
