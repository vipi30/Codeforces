import sys 

read = sys.stdin.read().split()
t = int(read[0])
indice = 1
res = []

for _ in range(t): 
    s = read[indice]
    indice += 1

    c = [0] * 10
    for i in s: 
        c[ord(i) - ord('0')] += 1
    
    actual = []
    for necesito in range(9, -1, -1):  
        for d in range(necesito, 10):
            if c[] > 0:
                c[d] -= 1
                actual.append(str(d))
                break
    res.append(''.join(actual))

print(*res, sep='\n')

