'''Crie um programa que tenha uma função leiaint(), que vai
funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas valor numérico.

Ex:.
n = leiaint('Digite um n')'''

#Minha resolução ↓
# def leiaint(msg=''):
#     '''
#     → input de números inteiros
#     :param msg: mensagem convertida em input
#     :return: retorna num, se apenas for número
#     '''
#     print('-' * 30)
#     while True:
#         num = input(msg)
#         if not num.isdigit():
#             print('\033[31m'+'ERRO! Digite um número inteiro válido.','\033[m')
#             continue
#         else:
#             num = int(num)
#             return num
#
#
# # n = int(input('Digite um número: '))
# n = leiaint('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! digite um número válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')