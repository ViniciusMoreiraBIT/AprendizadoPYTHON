'''Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: inicio, fim e passo e realiza a contagem.
  Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

from time import sleep

# Minha resolução ↓
'''def linha():
    print('-=' * 30)


def contador(i,f,p):
    linha()
    if p == 0: #Se passo for 0 então vira 1
        p = 1
    if p < 0: #Se passo for negativo então p recebe -x
        p = -p
    if i > f: #Se início for maior que fim, então p fica negativo e fim diminui 1
        p = -p
        f = f - 1
    if i < f: #Se fim for maior que início então fim aumenta 1
        f += 1
    p <= 0 and print(f'Contagem de {i} até {f + 1} de {p -  p - p} em {p - p - p}')
    i < f and print(f'Contagem de {i} até {f - 1} de {p} em {p}')
    for v in range(i,f,p):
        sleep(0.3)
        print(v, end=' ')
    sleep(0.3)
    print('FIM!')

contador(1,10,1)
contador(10,0,2)
linha()
contador(int(input('Início: ')),int(input('Fim: ')),int(input('Passo: ')))
linha()'''

def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
        print(f'FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
        print('FIM!')

contador(1,10,1)
contador(10,0,2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início:  '))
fim = int(input('Fim:     '))
passo = int(input('Passo: '))
contador(ini,fim,passo)