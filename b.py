    import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for _ in range(t): 
    n = int(next(read))
    s = next(read)

    if '0' not in s: 
        print(0)
        continue
    #guardo las posiciones donde hay '1'.
    unos = []
    for i in range(n): 
        if s[i] == '1': 
            unos.append(i)

    #como es ciclo
    pos_uno = unos[0] 
    unos.append(pos_uno + n)
    
    #esto lo hago para saber cuantos huecos hay entre cada '1'.
    espaciomax = 0 
    for j in range(len(unos)): 
        espacio = unos[j] - unos[j-1] 
        if espaciomax < espacio: 
            espaciomax = espacio 

    print(espaciomax - 1)

    


