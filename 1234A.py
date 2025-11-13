import math
q = int(input())

for i in range(q): 
    n = int(input())
    a = list(map(int, input().split()))
    
    x = sum(a)
    res = math.ceil(x/n)
    print(res)
