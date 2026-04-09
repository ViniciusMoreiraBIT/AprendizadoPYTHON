'''Crie um programa qie leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é
a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)'''

#Minha resolução ↓
'''soma = quant = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    quant += 1
print(f'A soma dos {quant} valores foi {soma}!')'''

soma = cont = 0
while True:
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'Você digitou {cont} números e a soma dos valores foi {soma}')
