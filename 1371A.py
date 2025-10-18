import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
   n = int(next(read))
   print((n+1)//2)
