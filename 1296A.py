import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    n = int(next(read))
    a = [int(next(read)) for _ in range(n)] #ya he terminado de leer el input.

    pares = 0
    impares = 0

    '''
    Si hay al menos un inpar, la condición se cumple. 
    Si todos son pares, no se cumple. 
    Si hay n cantidad de pares y esa n es par, no se cumple.
    '''
    for numero in a: 
        if numero % 2 == 0: 
            pares += 1
        else: 
            impares += 1

    if pares > 0 and impares > 0: 
        print('YES')  #me aseguro de que hay imapres pero que no lo sean todos. 

    elif impares == 0: 
        print('NO')

    elif pares == 0 and n % 2 == 0: #si no hay pares y la cnatidad de numeros es par.
        print('NO')

    else: 
        print('YES')
        
        
