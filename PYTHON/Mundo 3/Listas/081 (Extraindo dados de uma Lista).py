'''Crie um programa que vai ler vários números e colacar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores ordenada de forma descrescente.
c) Se o valor 5 foi digitado e está ou não na lista.'''

nuns = []

#Minha Resolução ↓
'''while True:
    nuns.append(int(input('Digite um Valor: ')))
    res = str(input('Quer continuar ? [S/N] ')).strip().upper()
    while res not in 'SN':
        res = str(input('Quer continuar ? [S/N] ')).strip().upper()
    if res == 'S':
        continue
    else:
        break

nunsr = list(reversed(nuns)) #cria uma nova lista em ordem decrescente
nunsr.sort(reverse=True)
#nuns.reverse() #←altera a original
print(f'Você digitou {len(nuns)} elementos.')
print(f'Os valores em ordem decrescente são {nunsr}')
print('O valor 5 faz parte da lista'if 5 in nuns else 'O valor 5 NÃO faz parte da lista')'''

while True:
    nuns.append(int(input('Digite um valor: ')))
    res = str(input('Quer continuar? [S/N] ')).upper().strip()
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).upper().strip()
    if res in 'N':
        break

print(f'Você digitou {len(nuns)} elementos.')
nuns.sort(reverse=True)
print(f'Os valores em ordem decrescente são {nuns}.')
5 in nuns and print('O valor 5 faz parte da lista!')
5 not in nuns and print('O valor 5 NÃO faz parte da lista!')