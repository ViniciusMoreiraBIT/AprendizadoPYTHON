'''Crie um programa que tenha uma função chamada voto() que
vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem
voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''

# Minha resolução ↓

# from datetime import datetime
#
# def voto(ano):
#     if ano < 18:
#         return False
#     elif ano < 65:
#         return True
#
#
# print('-'*30)
# nasc = datetime.now().year - int(input('Em que ano você nasceu? '))
# opc = voto(nasc)
#
# print(f'Com {nasc} anos:', end=' ')
# if opc == True:
#     print('VOTO OBRIGATÓRIO!')
# elif opc == False:
#     print('NEGADO!')
# else:
#     print('VOTO OPCIONAL!')


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÂO VOTA.'
    elif 16 <= idade <18 or idade > 65 :
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


#Programa principal
while True:
    nasc = int(input('Em que ano você nasceu? '))
    print(voto(nasc))