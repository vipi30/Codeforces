import sys 

read = sys.stdin.read().split()
t = int(read[0])
indice = 1
res = []

for i in range(t): 
    n = int(read[indice])
    x = int(read[indice+1])
    indice += 2
    
    a = list(map(int, read[indice:indice+n]))
    indice += n 

    if sum(a) == n*x: 
        res.append('YES')
    else: 
        res.append('NO')
sys.stdout.write('\n'.join(res))

