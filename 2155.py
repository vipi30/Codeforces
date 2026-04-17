import sys

read = iter(sys.stdin.read().split())
t = int(next(read))
res = []

for i in range(t): 
    n = int(next(read))
    ans = 2*n-2
    res.append(ans)
print(*res, sep='\n')
