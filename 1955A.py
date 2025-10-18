import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    n = int(next(read)) #helados que quiere
    a = int(next(read)) #precio de uno 
    b = int(next(read)) #precio de dos
    if b/2 < a: 
        if n % 2 == 0: 
            print((n//2)*b)
        else: 
            print((n//2)*b+a)
    else: 
        print(n*a)
