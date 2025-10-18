def solve(): 
    n, m = map(int,input().split())
    a = input()

    ans = 0

    for x in range(ord('A'), ord('H')): #-> es si enumerase los números con el valor que tienen aisgnado. 
        ans += max(0, m-a.count(chr(x))) # -> a.count cuenta cuantas veces aparece ese caracter en la cadena a. Chr convierte cada x al valor que tiene asignado.  
    print(ans)

t = int(input())

for i in range(t): 
    solve()
