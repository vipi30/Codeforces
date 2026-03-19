import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))
for i in range(t): 
    x = int(next(read)); y = int(next(read))
    if x+1 >= y and (x+1-y) % 9 == 0: 
        print('Yes')
    else:
        print('No')
