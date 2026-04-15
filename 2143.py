import sys

read = sys.stdin.read().split()
t = int(read[0]) 
indice = 1
res = []

for i in range(t): 
    n = int(read[indice])
    indice += 1 
    p = list(map(int, read[indice:indice+n])) 
    indice+= n

    l = 0 
    r = n-1 
    e = 1 
    bien = True 

    while l <= r: 
        if p[l] == e: 
            l+=1 
        elif p[r] == e: 
            r-=1 
        else:
            bien = False 
            break 
        e += 1 
    
    if bien == True:
        res.append('YES')
    else:
        res.append('NO')
print(*res, sep='\n')
