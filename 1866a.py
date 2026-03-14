import sys 

read = list(map(int, sys.stdin.read().split()))
t = int(read[0])
a = read[1:1+t]

res = min(abs(x) for x in a)
print(res)



