'''Crie um programa que tenha um função fatorial() que
receba dois parâmetros: o primeiro que indique o
número a calcular e o outro chamada show, que será
um valor lógico (opcional) indicando se será
mostrado ou não na tela o processo de cálculo do fatorial.'''


#Minha resolução
# def fatorial(num, show=False):
#     '''
#     → Fatorial de um número
#     :param num: Número escolhido
#     :param show: (Opcional) Mostrar ou não a conta
#     :return: o valor Fatorial de um número num.
#     '''
#     f = 1
#     for i in range(num, 0, -1):
#         f *= i
#         if show:
#             print(i, end='')
#             i > 1 and print(' x ', end='')
#             i == 1 and print(' = ', end='')
#     return f
#
# print('-'*30)
# fat = fatorial(5, True)
# print(fat)
# # help(fatorial)

def fatorial(n, show = False):
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa principal
print(fatorial(5,show=True))
