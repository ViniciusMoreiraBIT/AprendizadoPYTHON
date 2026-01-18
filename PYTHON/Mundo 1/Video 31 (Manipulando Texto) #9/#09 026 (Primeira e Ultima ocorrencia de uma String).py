'''Faça um programa que leia a Frase pelo teclado e mostre:

Quantas vezes aparece a letra 'A'
Em que posição ela aparece a primeira vez
Em que posição ela aparece a ultima vez '''

nome=str(input('Digite uma frase: ')).strip().upper()
print(f'Quantas vezes aparece a letra A: {nome.count('A')}') #nome.upper().count('A') daria também, mas daria erros nos outros que seria minusculo
print(f'Em que posição aparece a primeira vez: {nome.find('A') + 1}') #+1 pro usuario identificar
print(f'Em que posição aparece a ultima vez: {nome.rfind('A') + 1}')  #+1 pro usuario identificar

