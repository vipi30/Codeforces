import sys

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    n = int(next(read))
    a = [int(next(read)) for _ in range(n)]

    total = 0
    ceros = 0

    for x in a: 
        total += x 
        if x == 0: 
            ceros+=1
    print(total+ceros)


    

