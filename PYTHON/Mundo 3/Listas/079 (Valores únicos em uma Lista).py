'''Crie um programa onde o usúario possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados,
em ordem crescente'''

#Minha Resolução ↓
'''nuns = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in nuns:
        nuns.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    res = str(input('Quer continuar? [S/N] ')).upper()
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).upper()
    if res == 'S':
        continue
    elif res == 'N':
        break

#print(sorted(nuns)) ← mostra ordenado mas não altera a origiral
#nuns.sort() ← altera a origiral no crescente
#print(nuns) ← ja mostra com alteração

print('-=' * 20)
print(f'Você digitou os valores:',*sorted(nuns)) # o "*" tira os colchetes na hora de mostrar a lista'''

numeros = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('valor adicionado com Sucesso!')
    else:
        print('Valor duplicado. ERRO')
    r = str(input('Quer Continuar? [S/N]')).strip()
    if r in 'Nn':
        break
    elif r in 'Ss':
        continue

numeros.sort()
print('=-' * 30)
print(f'VocÊ digitou os valores: {numeros}')