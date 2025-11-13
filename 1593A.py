import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    a = int(next(read))
    b = int(next(read))
    c = int(next(read))
    if a > b and a > c: 
        A = 0 
    else: 
        A = max(b, c) + 1 - a 
    if b > a and b > c: 
        B = 0
    else: 
        B = max(a, c) + 1 - b
    if c > a and c > b: 
        C = 0
    else: 
        C = max(a, b) + 1 - c
    
    print(A, B, C)
