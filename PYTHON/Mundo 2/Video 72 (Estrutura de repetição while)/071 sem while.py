valor = int(input('Valor: R$ '))

cinquenta = valor // 50
valor %= 50
vinte = valor // 20
valor %= 20
dez = valor // 10
valor %= 10
um = valor // 1
valor %= 1

cinquenta >= 1 and print(f'{cinquenta} notas de 50.')
vinte >= 1 and print(f'{vinte} notas de 20.')
dez >= 1 and print(f'{dez} notas de 10.')
um >= 1 and print(f'{um} notas de 1.')



