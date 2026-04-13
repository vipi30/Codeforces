import sys

read = sys.stdin.read().split()
t = int(read[0])
indice = 1 
res = []

for i in range(t): 
    a = int(read[indice])
    indice += 1
    b = int(read[indice])
    indice+=1 
    c = int(read[indice])
    indice+=1 
    d = int(read[indice])
    indice+=1
    
    x1 = max(a,b)
    x2 = max(c-a, d-b)
    y1 = min(a,b)
    y2 = min(c-a, d-b)

    if x1 <= 2*(y1 +1) and x2 <= 2* (y2+1): 
        res.append('YES')
    else:
        res.append('NO')    
print(*res, sep = '\n')

    

