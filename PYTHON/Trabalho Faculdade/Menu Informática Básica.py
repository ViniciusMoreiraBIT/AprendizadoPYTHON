from datetime import date
while True:
    print('=-' * 10)
    print('MENU DE APRENDIZADO')
    print('=-' * 10)
    print('Digite o número da opção que você deseja.\n(1) Informática Básica.\n(2) Calculos Matemáticos.\n(3) Calcular sua idade.\n')
    res = int(input('R: '))
    if res == 2:
        while True:
            print('\nQual calculo deseja fazer?\n(1) Soma\n(2) Multiplicação\n(3) Subtração\n(4) Divisão\n(5) VOLTAR\n')
            n = input('R: ')
            if not n.isdigit():
                continue
            else:
                n = int(n)
                if n == 5:
                    print('')
                    break
                elif n == 1:
                    n1 = input('Primeiro Número: ')
                    n2 = input('Segundo Número: ')
                    if '.' in n1 or '.' in n2:
                        n1 = float(n1)
                        n2 = float(n2)
                    else:
                        n1 = int(n1)
                        n2 = int(n2)
                    print(f'{n1} + {n2} = {n1 + n2}')
                    continue
                elif n == 2:
                    n1 = input('Primeiro Número: ')
                    n2 = input('Segundo Número: ')
                    if '.' in n1 or '.' in n2:
                        n1 = float(n1)
                        n2 = float(n2)
                    else:
                        n1 = int(n1)
                        n2 = int(n2)
                    print(f'{n1} x {n2} = {n1 * n2:.2f}')
                    continue
                elif n == 3:
                    n1 = float(input('Primeiro Número: '))
                    n2 = float(input('Segundo Número: '))
                    print(f'{n1} - {n2} = {n1 - n2:.0f}')
                    continue
                elif n == 4:
                    n1 = float(input('Primeiro Número: '))
                    n2 = float(input('Segundo Número: '))
                    print(f'{n1} % {n2} = {n1 / n2}')
                    continue
                else:
                    print('ERRO...')
                    continue
    elif res == 3:
        ano = int(input('Ano de nascimento: '))
        mes = int(input('Mês de nascimento: '))
        dia = int(input('Dia de nascimento: '))
        hoje = date.today()
        nascimento = date(ano, mes, dia)
        print(f'\nVocê tem {hoje.year - nascimento.year} anos ({(hoje - nascimento).days} dias vividos)\n' )




