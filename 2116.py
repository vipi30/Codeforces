import sys
from math import gcd

read = sys.stdin.read().split()
t = int(read[0])
indice = 1
res = []

for i in range(t): 
    a = int(read[indice])
    b = int(read[indice+1])
    c = int(read[indice+2])
    d = int(read[indice+3])
    indice+=4
    
    if min(a, c) >= min(b, d): 
        res.append('Gellyfish')
    else: 
        res.append('Flower')
   
print(*res, sep = '\n')
