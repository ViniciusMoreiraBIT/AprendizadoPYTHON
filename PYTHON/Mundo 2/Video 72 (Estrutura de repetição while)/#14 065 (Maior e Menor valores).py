'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos. O progama deve
perguntar ao usúario se ele quer ou não continuar a digitar valores.'''

lista = []
print('Digite vários valores, no final vamos mostrar a média desses valores e o Maior! 999 para parar.')
loop = 0
soma = 0
while True:
    n = int(input(f'{loop + 1}º Valor: '))
    if n != 999:
        soma += n
        loop += 1
        lista.append(n)
    if n == 999:
        media = soma / loop
        print(f'A Média foi: {media:.2f}')
        res = input(f'O maior número digitado foi: {max(lista)}\nO menor número digitado foi {min(lista)}\nDeseja adicionar mais valores? (S/N)')
        if res.upper() == 'S':
            continue
        elif res.upper() == 'N':
            break
    else:
        continue
