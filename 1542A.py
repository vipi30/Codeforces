t = int(input())

for i in range(t): 
    n = int(input())
    a = list(map(int, input().split()))

    pares = 0
    impares = 0

    for x in a: 
        if x % 2 == 0: 
            pares +=1
        else: 
            impares +=1

    if pares == n and impares == n: 
        print('Yes')
    else: 
        print('No')
