import sys

read = sys.stdin.read().split()
t = int(read[0])
indice = 1 
res = []

for i in range(t): 
    n = int(read[indice])
    indice += 1
    a = list(map(int, read[indice:indice+n]))
    indice += n

    vistos = set()
    p = False

    for x in a: 
        if x in vistos: 
            p = True 
            break
        vistos.add(x)

    if p:
        res.append('YES')
    else:
        res.append('NO')

print(*res, sep = '\n')

    

