'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usúario digitar 999, que é a condição
de parada. No final, mostre quantos números foram digitados e qual
foi a soma entre eles(desconsiderando o flag)'''
loop = 1
soma = 0
print('Digite vários Números para a soma.. e 999 para parar!\n')
while True:
    n = int(input(f'{loop}º Número: '))
    loop += 1
    if n == 999:
        break
    else:
        soma += n
        continue
print(soma)



