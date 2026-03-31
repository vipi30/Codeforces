import sys
from math import gcd

read = sys.stdin.read().split()
t = int(read[0])
indice = 1
res = []

for i in range(t): 
    n = int(read[indice])
    indice+=1
    m = int(read[indice])
    indice+=1
    p = int(read[indice])
    indice+=1
    q = int(read[indice])
    indice+=1
    
    if n % p == 0: 
        if m == (n//p) * q: 
            res.append('Yes')
        else: 
            res.append('No')
    else: 
        res.append('Yes')
   
print(*res, sep = '\n')
