import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    a = int(next(read))
    b = int(next(read))
    c = int(next(read))
    n = int(next(read))
    
    #miro a ver cuál es el mayor nº entre a,b,c. 
    mx = max(a, b, c) 
    necesito = (mx-a) + (mx-b) + (mx-c)

    if n >= necesito and (n-necesito) % 3 == 0: #si n es menor que las monedas que necesito para poder repartirlas, no tendrán todas la misma cantidad.
        print('YES')
    else: 
        print('NO')
