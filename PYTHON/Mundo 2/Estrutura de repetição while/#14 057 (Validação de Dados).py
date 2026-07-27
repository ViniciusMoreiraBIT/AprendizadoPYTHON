'''Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores M ou F. Caso esteja errado,
peça a digitação novamente até ter um valor correto.'''

#minha resolução ↓
'''print('Responda M para masculino e F para feminino.')
while True:
    sexo = input('Qual seu sexo[M/F]? ').upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('Valor invalido.')
        continue
    elif sexo == 'M':
        print('Você é HOMEM')
        break
    else:
        print('Você é MULHER')
        break'''

res = str(input('Informe seu sexo (M/F): ')).strip().upper()[0] #[0] pega apenas a primeira letra
while res not in 'MF':
    res = str(input('Informe apenas M ou F: ')).upper().strip()[0]
if res == 'M':
    res ='Masculino'
else:
    res ='Feminino'

print(f'Sexo registrado com Sucesso: {res}')
