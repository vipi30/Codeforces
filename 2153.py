import sys

read = iter(sys.stdin.read().split())
t = int(next(read))
res = []

for i in range(t): 
    n = int(next(read))
    b = [int(next(read)) for _ in range(n)]
    b = set(b)
    res.append(len(b))
print(*res, sep='\n')
