import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    a = int(next(read))
    b = int(next(read))
    k = int(next(read))
    if k % 2 == 0: 
        res = (a-b) * (k//2)
    else: 
        res = (a-b) * (k//2) + a
    print(res)
    
