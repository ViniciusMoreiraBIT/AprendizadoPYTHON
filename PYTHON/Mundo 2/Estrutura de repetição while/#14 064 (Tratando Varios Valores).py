'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usúario digitar 999, que é a condição
de parada. No final, mostre quantos números foram digitados e qual
foi a soma entre eles(desconsiderando o flag)'''

#Minha resolução ↓
'''loop = 1
soma = 0
quant = 0
print('Digite vários Números para a soma.. e 999 para parar!\n')
while True:
    n = int(input(f'{loop}º Número: '))
    loop += 1
    if n == 999:
        break
    else:
        soma += n
        quant += 1
        continue
print(f'Você digitou {quant} números e a soma entre eles foi {soma}')'''

num = cont = soma = 0
num = int(input('Digite um Número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um Número: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')