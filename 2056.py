import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))
res = []
for i in range(t): 
    n = int(next(read)) #operaciones
    m = int(next(read)) #length
    p = 4*m

    for i in range(n):
        x = int(next(read)) #d
        y = int(next(read))

        if i > 0: 
            p+=2 * (x+y)
    
    res.append(p)
print('\n'.join(map(str, res)))

    
