import sys

read = sys.stdin.read().split()
t = int(read[0]) 
indice = 1
res = []

for i in range(t): 
    n = int(read[indice])
    indice += 1 
    a = read[indice:indice+n] 
    indice+= n

    f = []
    suma = 1 
    for j in range(1,n): 
        if a[j] == a[j-1]: 
            suma += 1 
        else: 
            f.append(suma)
            suma = 1 
    f.append(suma)
    
    mejor = 0
    maxf = max(f)

    for k in range(1, maxf +1): 
        cantidad = 0 
        for x in f: 
            if x >= k: 
                cantidad+=1 
        mejor = max(mejor, k*cantidad)
    res.append(mejor)

print(*res, sep='\n')
