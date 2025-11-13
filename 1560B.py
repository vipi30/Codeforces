import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    a = int(next(read))
    b = int(next(read))
    c = int(next(read))
    n = 2 * abs(a-b)
    
    if n < a or n < b or n < c: 
        print('-1')
        continue 
    if c + abs(a-b) <= n:
        print(c+abs(a-b))
    else: 
        print(c-abs(a-b))


