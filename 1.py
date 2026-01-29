#permutaciones 
#|pi−pi+1| is divisible by i for every 1≤i≤n−1.
import sys 
read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    n = int(next(read))

    lista = []
    l, r = 1, n #punteros
    while l <= r:
        lista.append(l)
        l += 1
        if l <= r:
            lista.append(r)
            r -= 1
    print(*lista[::-1])
