termo = int(input('Primeiro Termo: '))
PG = int(input('Razão: '))
for i in range(1, 11):
    print(f'{i} Termo (a{i}): {termo}')
    termo *= PG
