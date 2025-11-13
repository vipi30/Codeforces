import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    n = int(next(read))
    m = int(next(read))
    x = int(next(read))
    col = (x-1)//n 
    row = (x-1) % n 
    res = row*m + col+1 
    print(res)
