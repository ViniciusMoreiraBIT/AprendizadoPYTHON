'''Crie um programa onde o usuário possa digitar cinco valores
numéricos e cadatre-os em uma lista, já na posição correta de
inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''

nuns = []

#minha primeira resolução 100% sozinho ↓
'''cont = maior = menor = 0
for i in range (0, 5):
    n = int(input('Digite um valor: '))
    cont += 1
    if cont == 1:
        maior = n
        menor = n
        nuns.append(n)
        print('Adicionado no final da lista')

    elif n > maior:
        nuns.append(n)
        print('Adicionado no final da lista')
    elif n < menor:
        nuns.insert(0,n)
        menor = n 
        print('Adicionado na posição 0 da lista')
    elif n < maior and n > menor:
        nuns.insert(1,n)
        print('Adicionado na posição 1 da lista')

print(f'Os valores digitados em ordem foram {nuns}')'''

#segunda resolução ↓
'''for i in range (0, 5):
    n = int(input('Digite um valor: '))

    if i == 0 or n > nuns[-1]:
        nuns.append(n)
        print('Adicionado no final da Lista.')

    else:
        for i in range(0,len(nuns)):
            if n <= nuns[i]:
                nuns.insert(i,n)
                print(f'Adicionado na posição {i}')
                break

print(f'Os valores digitados em ordem foram {nuns}')'''

for i in range (0,5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > nuns[-1]:
        nuns.append(n)
        print('Adicionado no final da lista!')
    else:
        pos = 0
        while pos < len(nuns):
            if n <= nuns[pos]:
                nuns.insert(pos,n)
                print(f'Adicionado na posição {pos}!')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem é: {nuns}')
