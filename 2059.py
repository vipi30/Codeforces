import sys 

read = sys.stdin.read().split()
t = int(read[0])
indice = 1
salida = []

for i in range(t): 
    n = int(read[indice]) #operaciones
    indice +=1
    a = read[indice:indice + n]
    indice += n

    b = read[indice:indice + n]
    indice += n

    if len(set(a)) + len(set(b)) >= 4:
        salida.append("YES")
    else:
        salida.append("NO")

sys.stdout.write("\n".join(salida))
    
