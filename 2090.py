import sys 

read = sys.stdin.read().split()
t = int(read[0])
indice = 1
res = []

for i in range(t): 
    x = int(read[indice])
    y = int(read[indice+1])
    a = int(read[indice+2])
    indice += 3
    
    f = a // (x+y)
    d = f*(x+y)

    if d + x > a: 
        res.append('no')
    else: 
        res.append('yes')
sys.stdout.write('\n'.join(res))

