n = list(map(int, input().split())) #map es para transformar de palabras a numeros enteros.

n.sort() #ordenar los n de menor a mayor.

a = n[3]-n[0] #el mayor de los 4 numeros será n[3]
b = n[3]-n[1]
c = n[3]-n[2]

print(a, b, c)
