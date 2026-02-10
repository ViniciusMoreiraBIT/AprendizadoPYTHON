'''Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores M ou F. Caso esteja errado,
peça a digitação novamente até ter um valor correto.'''

print('Responda M para masculino e F para feminino.')
while True:
    sexo = input('Qual seu sexo[M/F]? ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Valor invalido.')
        continue
    elif sexo == 'M':
        print('Você pe HOMEM')
        break
    else:
        print('Você é MULHER')
        break

