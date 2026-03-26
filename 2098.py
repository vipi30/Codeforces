t = int(input())
res = []

for _ in range(t):
    s = input().strip()

    c = [0] * 10
    for i in s:
        c[ord(i) - ord('0')] += 1
    
    actual = []
    for necesito in range(9, -1, -1):
        for d in range(necesito, 10):
            if c[d] > 0:
                c[d] -= 1
                actual.append(str(d))
                break

    res.append(''.join(actual))

print('\n'.join(res))
