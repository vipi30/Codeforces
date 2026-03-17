import sys 

read = sys.stdin.read().split()
t = int(read[0])
indice = 1
salida = []
for i in range(t): 
    n = int(read[indice]) #operaciones
    m = int(read[indice +1]) #length
    indice +=2

    if n == 1: 
        res = 1
    else: 
        res = 0
    res += max(0, m - max(n, 2))
    salida.append(str(res))

sys.stdout.write("\n".join(salida))
    
