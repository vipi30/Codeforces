import sys 

read= iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t):
    x = int(next(read))
    y = int(next(read))
    n = int(next(read))
    k = n - (n-y) % x
    print(k)

