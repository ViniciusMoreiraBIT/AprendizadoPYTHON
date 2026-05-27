valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for i in range (1,4):
    valores.append(int(input('Digite um valor: ')))

for i,v in enumerate(valores):
    print(f'{i} {v} ')