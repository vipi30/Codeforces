import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))
min_dia = 24*60

for i in range(t): 
    h = int(next(read))
    m = int(next(read))
  
    h = h * 60 #paso las horas a minutos. 
    x = min_dia - (h + m)

    print(x)
