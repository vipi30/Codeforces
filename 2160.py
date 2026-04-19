import sys

read = iter(sys.stdin.read().split())
t = int(next(read))
res = []

for i in range(t): 
    n = int(next(read))
    c = [0] * 101 

    for _ in range(n): 
        c[int(next(read))] += 1 

    for j in range(101): 
        if c[j] == 0: 
            res.append(j)
            break 
print(*res, sep = '\n')

