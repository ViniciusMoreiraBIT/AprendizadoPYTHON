'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos. O progama deve
perguntar ao usúario se ele quer ou não continuar a digitar valores.'''

numbers = []
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
    if n == 999:
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
        continue
