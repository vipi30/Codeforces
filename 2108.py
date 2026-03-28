import sys 

read = sys.stdin.read().split()
t = int(read[0])
res = []

for i in range(1, t+1): 
    n = int(read[i])
    res.append(n**2//4 + 1)

print(*res, sep='\n')
