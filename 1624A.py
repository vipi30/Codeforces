import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    n = int(next(read))
    a = [int(next(read)) for j in range(n)]   #para que lo lea como una lista
    a.sort()
    print(a[-1]-a[0])

