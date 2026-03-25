import sys 

read = list(map(int, sys.stdin.read().split()))
t = int(read[0])
indice = 1
res = []

for i in range(t): 
    n = int(read[indice])
    indice += 1
    a = read[indice:indice+n]
    indice+=n
    
    res.append(str(len(set(a))))

print(*res, sep='\n')

