import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    a = int(next(read))
    b = int(next(read))
    d = int(next(read))
    
    x = abs(a-b)
    y = min(a, b)

    if d == 0 and a == b: 
        print('YES')
    elif x / y <= d: 
        print('YES') 
    else:
        print('NO')
