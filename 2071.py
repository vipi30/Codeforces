import sys 

read = sys.stdin.read().split()
t = int(read[0])
res = []

for i in range(1, t+1): 
    k = int(read[i])
    if k % 3 == 1: 
        res.append('YES')
    else: 
        res.append('NO')
sys.stdout.write('\n'.join(res))

