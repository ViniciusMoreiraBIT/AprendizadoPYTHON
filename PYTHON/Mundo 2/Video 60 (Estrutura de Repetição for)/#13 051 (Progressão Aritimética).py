'''Desenvolva um programa que leia o
primeiro termo e a razão de uma PA. No
final, mostre os 10 primeiros termos dessa progressão'''

'''termo = int(input('Primeiro termo: '))
PA = int(input('Razão da PA: '))
for i in range (1, 11):
    valor = termo + (i - 1) * PA
    print(f'{i} Termo (a{i}): {valor}')'''

primeiro=int(input('Primeiro Termo: '))
razao=int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
cont = 1
for i in range(primeiro, decimo + razao, razao ):
    print(f'{cont} Termo (a{cont}): {i}')
    cont+=1

