import sys

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    n = int(next(read))
    k = int(next(read))
    ans = '1' * k + '0' * (n-k)
    print(ans)

