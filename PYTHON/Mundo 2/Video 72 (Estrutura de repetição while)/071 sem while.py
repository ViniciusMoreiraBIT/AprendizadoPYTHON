valor = int(input('Valor: R$ '))

cinquenta = valor // 50 #“quantas vezes o número 50 cabe dentro de valor ex:. 287 // 50 = 5”
valor %= 50 #o que sobrou depois de tirar X 50 de valor ex:. 287 % 50 = 37 ?
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



