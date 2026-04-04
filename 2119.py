import sys

read = sys.stdin.read().split()
t = int(read[0])
res = []
indice = 1

for i in range(t): 
    a = int(read[indice])
    b = int(read[indice+1])
    x = int(read[indice+2])
    y = int(read[indice+3])
    indice+=4 

    if a == b: 
        res.append('0')
        continue

    if a > b: 
        if a%2 == 1 and b == a - 1: 
            res.append(y)
        else: 
            res.append('-1')
        continue 
    
    d = b - a 
    c = min(x, y)
    
    if a % 2 == 0: 
        pasos_p = (d+1) // 2
        pasos_i = d//2 
    else: 
        pasos_i = (d+1) // 2
        pasos_p = d // 2 
    total = pasos_p * c + pasos_i * x
    res.append(total)
print(*res, sep = '\n')

     

