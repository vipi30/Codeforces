import sys

read = sys.stdin.read().split()
t = int(read[0])
res = []
indice = 1

for i in range(t): 
    n = int(read[indice])
    indice+= 1
    c = int(read[indice])
    indice+=1 
    pesos = list(map(int, read[indice:indice+n]))
    indice += n 
    
    lista = [] 

    for peso in pesos: 
        if peso <=c: 
            q = c // peso
            l = q.bit_length() - 1 
            lista.append(l)
    lista.sort() 
    
    coste = 0 
    for x in lista: 
        if coste <= x: 
            coste += 1
    res.append(n-coste)
print(*res, sep = '\n')



