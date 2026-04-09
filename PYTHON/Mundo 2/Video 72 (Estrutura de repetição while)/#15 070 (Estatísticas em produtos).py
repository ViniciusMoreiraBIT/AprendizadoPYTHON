'''Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato'''

#Minha resolução ↓
'''total = maismil = rep = 0
barato = ''
while True:
    while True:
        nome_produto = input('Nome do Produto: ')
        if not nome_produto.isalpha():
            continue
        else:
            break
    while True:
        preco = input('Preço: R$')
        if not preco.isdigit():
            continue
        else:
            preco = float(preco)
            break
    total += preco
    rep += 1
    if preco > 1000:
        maismil += 1
    if rep == 1:
        precomenor = preco
        barato = nome_produto
        custo = preco
    if preco < precomenor :
        barato = nome_produto
        custo = preco

    while True:
        per = input('Quer continuar ? (S/N): ').strip().upper()
        if per not in ('S','N'):
            continue
        else:
            break
    if per == 'S':
        continue
    elif per == 'N':
        if rep == 1:
            barato = nome_produto
            custo = preco
    break

print('-'*10,'FIM DO PROGRAMA','-' * 10)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maismil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {barato} custando R${custo:.2f}')'''

barato = ''
total = totmil = menor = cont = 0
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    resp = ' '
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{'Fim do Programa!':-^40}')
print(f'O total da compra foi: R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000')
print(f'O pruduto mais barato é o {barato } custando R${menor}')
