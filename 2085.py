import sys 

read = sys.stdin.read().split()
t = int(read[0])
indice = 1
res = []

for i in range(t): 
    n = int(read[indice])
    k = int(read[indice+1])
    indice += 2
    
    s = read[indice]
    indice += 1

    if s < s[::-1]: 
        res.append('YES')
    elif k == 0: 
        res.append('NO')
    elif len(set(s)) == 1: 
        res.append('NO')
    else:
        res.append('YES')
sys.stdout.write('\n'.join(res))

