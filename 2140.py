import sys

read = sys.stdin.read().split()
t = int(read[0]) 
indice = 1
res = []

for i in range(t): 
    n = int(read[indice])
    s = read[indice+1]
    indice+=2

    ceros = s.count('0')
    pr = s[:ceros]
    ans = pr.count('1')
    res.append(ans)
print(*res, sep='\n')
    
    
    

    

