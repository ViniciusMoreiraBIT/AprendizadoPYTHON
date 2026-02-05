lista = ['a','b','c','d','e']

for i in lista:
    print(i)

print('-'*10)

for item, i in enumerate(lista):
    print(i , item)

print('-'*10)

for i in range(5):
    #print(lista[i])
    print(lista[i], i)

print('-'*10)

i=0
while i < 5:
    print(lista[i], i)
    i += 1