import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    n = int(next(read))
    sitios = next(read)

    if '1' not in sitios: 
        print(n//2) 
    
    else: 
        unos = sitios.count('1')
        #cuento los posibles: 
        bloques = sitios.split('1') #bloques solo de ceros
        añadir = 0 

        for j in range(len(bloques)): 
            cantidad = len(bloques[j])
            if j == 0 or j == len(bloques) -1: 
                añadir += cantidad//3
            else:
                if cantidad >= 3: 
                    añadir += (cantidad-2) // 3
                else: 
                    añadir += 0
        print(unos+añadir)
