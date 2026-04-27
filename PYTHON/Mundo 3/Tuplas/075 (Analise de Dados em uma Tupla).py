'''Desenvolva um programa que leia 4 valores pelo teclado e garde-os em uma tupla.
No final mostre:
a)Quantas vezes apareceu o valor 9.
b)Em que posição foi digitado o primeiro 3.
c) Quais foram os numeros pares'''

#Minha resolução ↓
'''print('Digite quatro valores.')
n1 = int(input('Valor: '))
n2 = int(input('Valor: '))
n3 = int(input('Valor: '))
n4 = int(input('Valor: '))
nuns = (n1, n2, n3, n4)
print(f'Seus números:' ,*nuns)
print(f'O valor 9 apareceu {nuns.count(9)} vez'if nuns.count(9) == 1 else f'O valor 9 apareceu {nuns.count(9)} vezes')
print(f'O primeiro 3 apareceu na {nuns.index(3) + 1}º posição'if 3 in nuns else 'O valor 3 não foi digitado.')
sim = 0
for numero in nuns:
    if numero % 2 == 0:
        sim = 1
if sim == 0:
    print('Nenhum número par')
elif sim == 1:
    print('Os valores pares digitados foram: ' , end='')
    for numeros in nuns:
        if numeros % 2 == 0:
            print(numeros, end= ' ')'''

num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou os valores {num}')
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)} vezes.')
else:
    print('O valor 9 não foi digitado.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram ',end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')