import sys
from math import gcd

read = sys.stdin.read().split()
t = int(read[0])
indice = 1
res = []

for i in range(t): 
    n = int(read[indice])
    indice+=1

    a = list(map(int, read[indice:indice+n]))
    indice += n

    g = 0

    for numero in a:
        g = gcd(numero,g)

    ind = -1
    for j in range(n): 
        if a[j] != g: 
            ind = j
            break 
    if ind == -1: 
        res.append('No')
    else: 
        res.append('Yes')
        ans = ["2"] * n
        ans[ind] = "1"
        res.append(" ".join(ans))

print(*res, sep='\n')
