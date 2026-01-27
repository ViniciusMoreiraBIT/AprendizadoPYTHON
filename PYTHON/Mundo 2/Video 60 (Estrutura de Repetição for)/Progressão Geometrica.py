termo = int(input('Primeiro Termo: '))
PA=int(input('Progressão: '))
'''for i in range(1, 11):
    valor = termo + (i - 1) * PA
    print(f'{i} Termo (a{i}): {valor}')'''
valor= 0
for i in range(1, 11):
    print(f'{i} Termo (a{i}): {valor}')
    valor += (PA ** i)