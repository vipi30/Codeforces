import sys

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    n = int(next(read))
    a = [int(next(read)) for _ in range(n)]

    total = sum(a)

    if 0 in a: 
        total+= 1
    print(total)


    

