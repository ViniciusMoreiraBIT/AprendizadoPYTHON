'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.'''

#Minha resolução sem while ↓
'''print('Teste de Vogais nas palavras:\n')
palavra = ('Aprender','Caderno','Linguagem','Python','Curso','Gratis','Estudar','Praticar','Trabalhar','mercado','programador','futuro')
for p in palavra:
    print(f'Na palavra {p.upper()} temos',end=' ')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')
    print('')'''

#Minha resolução com while ↓
'''print('Teste de Vogais nas palavras:\n')
palavra = ('Aprender','Caderno','Linguagem','Python','Curso','Gratis','Estudar','Praticar','Trabalhar','mercado','programador','futuro')
cont = 0
while cont < len(palavra):
    p = palavra[cont]
    print(f'Na palavra {p.upper()} temos',end=' ')
    cont += 1
    for l in p:
        if l.upper() in 'AEIOU':
            print(l.upper(), end= ' ')
    print()'''

palavra = ('Aprender','Caderno','Linguagem',
           'Python','Curso','Gratis',
           'Estudar','Praticar','Trabalhar',
           'mercado','programador','futuro')
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')

