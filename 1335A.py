import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

resultado = []
for i in range(t): 
    n = int(next(read))
    res = (n-1)// 2
    resultado.append(str(res))

print("\n".join(resultado))
 
