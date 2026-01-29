import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    n = int(next(read))
    a = [int(next(read)) for _ in range(n)]
    pasos = 0
    
    minimo = a[0]

    for j in range(1, n): 
        if a[j] < minimo: 
            pasos += 1 
        else: 
            minimo = a[j]

    print(pasos)
