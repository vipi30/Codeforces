import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

salida = []
for i in range(t): 
    moves = 0
    a = int(next(read))
    b = int(next(read))
    if a % b == 0: 
        res = moves
    else: 
        res = b-(a%b)
    salida.append(str(res))
    
print("\n".join(salida))
