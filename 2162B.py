t = int(input())

for i in range(t): 
    n = int(input())
    s = input()
    
    pos = []
    for i, ch in enumerate(s):
        if ch == '0':
            pos.append(i + 1) 

    print(len(pos))
    print(*pos)    
