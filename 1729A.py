import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    a = int(next(read))
    b = int(next(read))
    c = int(next(read))
    t1 = abs(a-1)
    t2 = abs(b-c) + abs(c-1)

    if t1 == t2: 
        print('3')
    elif t2 < t1: 
        print('2')
    else: 
        print('1')
