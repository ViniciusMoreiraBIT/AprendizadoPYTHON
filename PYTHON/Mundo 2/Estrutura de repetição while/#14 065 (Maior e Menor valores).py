'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos. O progama deve
perguntar ao usúario se ele quer ou não continuar a digitar valores.'''

#Minha resolução ↓ (todos usei while True)
'''numbers = []
print('Digite vários valores, no final vamos mostrar a média desses valores e o Maior! 999 para parar.')
loop = 0
soma = 0
while True:
    n = input(f'{loop + 1}º Valor: ')
    if not n.isdigit():
        print('Apenas números!')
        continue
    else:
        n = int(n)

    if n != 999:
        soma += n
        loop += 1
        numbers.append(n)
    elif n == 999:
        media = soma / loop
        print(f'\nA Média foi: {media:.2f}')
        print(f'O maior número digitado foi: {max(numbers)}\nO menor número digitado foi: {min(numbers)}\n\nDeseja adicionar mais valores? (S/N)')
        while True:
            res = input('').upper()
            if res not in ('S','N'):
                print('Apenas S/N')
                continue
            elif res == 'S' or res == 'N':
                if res == 'S':
                    break
                elif res == 'N':
                    break
        if res == 'N':
            break
    else:
        continue'''

print('\nDigite vários valores, no final vamos mostrar a média desses valores e o Maior!')
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num  = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar [S/N] ? ')).upper().strip()
media += soma / quant
print(f'Você digitou {quant} números e a média foi {media:.2f}\nO maior número digitado foi: {maior}\nO menor número digitado foi: {menor}')