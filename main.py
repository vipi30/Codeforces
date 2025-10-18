t = int(input())

for i in range(t): 
    x, y, z = map(int, input().split())
    res = sorted([x, y, z])
    if res[1] != res[2]: 
        print('NO')
    else: 
        print('YES')
        print(res[0], res[2], res[0])
