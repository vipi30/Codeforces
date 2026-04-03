import sys
import math

read = sys.stdin.read().split()
t = int(read[0])
res = []
idx = 1

for i in range(t): 
    l1 = int(read[idx])
    idx += 1
    b1 = int(read[idx])
    idx += 1
    l2 = int(read[idx])
    idx += 1
    b2 = int(read[idx])
    idx += 1
    l3 = int(read[idx])
    idx += 1
    b3 = int(read[idx])
    idx += 1
    area = l1 * b1 + l2 * b2 + l3 * b3 

    s = int(math.isqrt(area))

    if s * s != area:
        res.append("NO")
        continue

    ok = False

    #vertical
    if l1 == s and l2 == s and l3 == s and b1 + b2 + b3 == s:
        ok = True

    elif l1 == s and b2 == b3 and b1 + b2 == s and l2 + l3 == s:
        ok = True
    
    elif b1 == s and l2 == l3 and l1 + l2 == s and b2 + b3 == s:
        ok = True

    if ok: 
        res.append('YES')
    else: 
        res.append('NO')

print(*res, sep='\n')


