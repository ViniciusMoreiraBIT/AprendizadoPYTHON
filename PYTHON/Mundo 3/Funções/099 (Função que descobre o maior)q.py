'''Faça umm programa que tenha uma função chmada maior(),
que recebá varios parâmetros com valores inteiros.
 Seu programa tem que analisar todas os valores e dizer
qual é o maior.'''
from time import sleep

# #Minha resolução ↓
# def maior(*n):
#     maior = qnt = 0
#     print('-=' * 30)
#     print('Analisando os valores passados...')
#     if len(n) != 0:
#         maior = max(n)
#         qnt = len(n)
#     for i in n:
#         sleep(0.3)
#         print(i, end=' ')
#     print(f'Foram informados {qnt} valores ao todo.')
#     print(f'O maior valor informado foi {maior}.')
#
# maior(2,9,4,5,7,1)
# maior(4,7,0)
# maior(1,2)
# maior(6)
# maior(0) # 0 conta como um valor, logo "len(n) == 1"
# maior()  # nada não é valor, logo "len(n) == 0

def maior(*n):
    cont = maior = 0
    print('-=' *30)
    print('Analisando os valores passados... ')
    for v in n:
        print(f'{v} ', end='' )
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
maior()