import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))
#pierde si no tiene más movimientos. miro la distancia
for i in range(t): 
    n = int(next(read))
    a = int(next(read))
    b = int(next(read))
    
    if abs(a-b) % 2 == 0: 
        print('YES')
    else:
        print('NO')
