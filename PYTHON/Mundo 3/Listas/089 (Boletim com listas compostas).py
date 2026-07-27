'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita
que o usúario possa mostrar notas de cada aluno individualmente '''

#Minha resolução ↓
'''
alunos = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    alunos.append([nome,n1,n2])
    res = str(input('Quer continuar ? [S/N] ')).strip().upper()
    while res not in 'NS':
        res = str(input('Quer continuar ? [S/N] ')).strip().upper()
    if res == 'N':
        break

print('-=' * 20)
print(f'{'No.': <5}{'NOME': <15}{'MÉDIA': >10}')
print('-'*30)
for i in range(0, len(alunos)):
    print(f'{i:<5}{alunos[i][0]: <15}{(alunos[i][1] + alunos[i][2]) / 2: >9.1f}')
print('-'*30)
while True:
    per = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if per == 999:
        break
    else:
        for i,v in enumerate(alunos):
            if per == i:
                print(f'Notas de {v[0]} são {v[1],v[2]}')
                print('-' * 30)'''

ficha = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome,[n1,n2],media])
    res = str(input('Quer continuar? [S/N]'))
    if res in 'Nn':
        break

print('=-' * 15)
print(f'{'No':<4}{'Nome:':<10}{'Média':>8}')
print('-' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:_<10}{a[2]:_>7.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar nostas de qual aluno? [999 interrompe]: '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')