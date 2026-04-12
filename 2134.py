import sys

read = sys.stdin.read().split()
t = int(read[0])
indice = 1 
res = []

for i in range(t): 
    n = int(read[indice])
    indice += 1
    a = int(read[indice])
    indice+=1 
    b = int(read[indice])
    indice+=1 
    
    if (n-b) % 2 != 0: 
        res.append('NO')

    elif (n-a) % 2 == 0: 
        res.append('YES')
    elif a <= b: 
        res.append('YES')
    else:
        res.append('NO')

print(*res, sep = '\n')

    

