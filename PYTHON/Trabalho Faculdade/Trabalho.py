from datetime import date
from time import sleep

def ler_numero(msg):
    while True:
        try:
            n = input(msg).replace(',','.')
            if '.' in n:
                return float(n)
            else:
                return int(n)
        except ValueError:
            print('Digite um número válido!')

while True:
    try:
        while True:
            print('=-' * 10)
            print('MENU DE APRENDIZADO')
            print('=-' * 10)
            print('Digite o número da opção que você deseja.\n(1) Sobre Computador\n(2) Calculos Matemáticos\n(3) Calcular sua idade\n(4) Tabuada\n(5) Encerrar Programa')
            res = int(input('R: '))
            if res not in (1,2,3,4,5):
                print('Apenas as opções presentes..')
                sleep(1)
                continue
            else:
                break
    except ValueError:
        print('Valor invalido.')
        sleep(1)
        continue
    if res == 2:
        while True:
            print('\nQual calculo deseja fazer?\n(1) Soma\n(2) Multiplicação\n(3) Subtração\n(4) Divisão\n(5) VOLTAR\n')
            try:
                n = int(input('R: '))
                if n not in (1,2,3,4,5):
                    print('Apenas as opções presentes..')
                    sleep(1)
                    continue
            except ValueError:
                print('Valor invalido.')
                sleep(1)
                continue
            if n == 5:
                print('Voltando', end='')
                for i in range(0,2):
                    sleep(0.5)
                    print('.', end='')
                sleep(0.5)
                print()
                break
            elif n == 1:
                n1 = ler_numero('Primeiro Número: ')
                n2 = ler_numero('Segundo Número: ')
                print(f'{n1} + {n2} = {n1 + n2}')
            elif n == 2:
                n1 = ler_numero('Primeiro Número: ')
                n2 = ler_numero('Segundo Número: ')
                print(f'{n1} x {n2} = {n1 * n2}')
            elif n == 3:
                n1 = ler_numero('Primeiro Número: ')
                n2 = ler_numero('Segundo Número: ')
                print(f'{n1} - {n2} = {n1 - n2}')
            elif n == 4:
                n1 = float(input('Primeiro Número: '))
                n2 = float(input('Segundo Número: '))
                while n2 == 0:
                    n2 = float(input('Não é possivel dividir por 0, tente outro número: '))
                resul = n1 / n2
                texto = str(resul)
                if '.' in texto and len(texto.split('.')[1]) > 2:
                    print(f'{n1} / {n2} = {n1 / n2:.3f}...')
                else:
                    print(f'{n1} / {n2} = {n1 / n2:.2f}')
            back = input('\nVoltar (ENTER)')
            while len(back) != 0:
                back = input('Voltar (ENTER)')
            else:
                continue

    elif res == 3:
        while True:
            hoje = date.today().year
            try:
                while True:
                    ano = input('Ano de nascimento: ')
                    if not ano.isdigit():
                        print('Apenas números..')
                    elif len(ano) != 4:
                        print('4 Digitos apenas..')
                    elif int(ano) > hoje:
                        print(f'Estamos no ano {hoje}..')
                    elif int(ano) <= 1900:
                        print('Você não é tão velho assim, mas já vi que isso é um teste..')
                        break
                    else:
                        break
                if len(ano) == 4:
                    ano = int(ano)
                    while True:
                        mes = input('Mês de nascimento: ')
                        if not mes.isdigit():
                            print('Apenas números..')
                        elif int(mes) <= 0:
                            print('De um valor válido de mês..')
                        elif len(mes) != 2:
                            print('2 Digitos apenas..')
                        elif int(mes) > 12:
                            print('No ano tem apenas 12 meses..')
                        else:
                             break
                    if len(mes) == 2:
                        mes = int(mes)
                        while True:
                            dia = input('Dia de nascimento: ')
                            if not dia.isdigit():
                                print('Apenas números')
                            elif int(dia) <= 0:
                                print('De um valor válido de dia..')
                            elif len(dia) != 2:
                                print('Apenas 2 digitos')
                            elif int(dia) > 31:
                                print('Até 31 dias..')
                            else:
                                break
                    if len(dia) == 2:
                        dia = int(dia)
                        hoje = date.today()
                        nascimento = date(ano, mes, dia)
                        idade = hoje.year - nascimento.year
                        if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
                            idade -= 1

                        print(f'Você tem {idade} anos ({(hoje - nascimento).days} dias vividos)\n')

                        back = input('Voltar (ENTER)')
                        while len(back) != 0:
                            back = input('Voltar (ENTER)')
                        else:
                            break

            except ValueError:
                print('Valor invalido')
                sleep(1)

    elif res == 1:
        while True:
            print('--' * 20)
            print(f'{'INTRODUÇÃO AO HARDWARE': ^40}')
            print('--' * 20)
            print('''Hardware representa todos os componentes
físicos de um computador.
        
Processador, memória RAM, SSD, placa de
vídeo e fonte são exemplos de hardware.

Neste módulo você poderá aprender sobre
os principais equipamentos de informática.

Qual deseja conhecer?
(1) Processador
(2) Placa-Mãe
(3) Memória RAM
(4) SSD / HD
(5) Placa de Vídeo
(6) Fonte de Alimentação
(7) Coolers
(8) Gabinete
(9) VOLTAR..''')
            try:
                opc = int(input(''))
                if opc == 1:
                    print(f'{'PROCESSADOR (GPU)':-^30}')
                    print('''
FUNÇÃO:
É o cérebro do computador.
Responsável por executar cálculos, processar
informações e executar programas.

LOCALIZAÇÃO:
Fica localizado na placa-mãe, preso em um
encaixe chamado socket.

ESTRUTURA: 
Possui formato quadrado e contém milhares
de pequenos contatos metálicos responsáveis 
pela comunicação com o sistema.
Na parte superior geralmente existem um cooler
para resfriamento, já que o processador
pode atingir temperaturas acima de 70 graus Celsius
''')

                elif opc == 2:
                    print(f'{'PLACA MÃE':-^30}')
                    print('''
FUNÇÃO:
Responsável pela comunicação entre todos os
componentes do computador.

LOCALIZAÇÃO:
Fica fixada dentro do gabinete.

ESTRUTURA:
É uma grande placa de circuito contendo slots,
conectores, trilhas elétricas e encaixes para
as demais peças.
''')

                elif opc == 3:
                    print(f'{'MEMÓRIA RAM':-^30}')
                    print('''
FUNÇÃO:
Armazena temporariamente os dados dos programas
que estão sendo utilizados no momento.

LOCALIZAÇÃO:
Fica conectada diretamente na placa-mãe em
slots específicos de memória.

ESTRUTURA:
Possui formato de uma placa fina e comprida,
contendo chips responsáveis pelo armazenamento
temporário de dados.
''')

                elif opc == 4:
                    print(f'{'SSD / HD':-^30}')
                    print('''
FUNÇÃO:
Responsáveis por armazenar arquivos, jogos,
fotos, vídeos e o sistema operacional.

LOCALIZAÇÃO:
Normalmente ficam instalados no gabinete e
conectados à placa-mãe através de cabos SATA
ou conexão M.2.

ESTRUTURA:

HD:
Possui partes mecânicas internas com discos
giratórios e braço de leitura.

SSD:
Não possui partes mecânicas, utilizando chips
de memória eletrônica, tornando-o muito mais
rápido e silencioso.
''')

                elif opc == 5:
                    print(f'{'PLACA DE VÍDEO (GPU)':-^30}')
                    print('''
FUNÇÃO:
Responsável pelo processamento gráfico do
computador.

LOCALIZAÇÃO:
Fica conectada na placa-mãe através do slot
PCI Express.

ESTRUTURA:
É uma placa grande contendo processador gráfico,
memórias próprias e sistema de refrigeração com
coolers.
''')

                elif opc == 6:
                    print(f'{'FONTE DE ALIMENTAÇÃO':-^30}')
                    print('''
FUNÇÃO:
Responsável por fornecer energia para todas
as peças do computador.

LOCALIZAÇÃO:
Geralmente fica na parte inferior traseira
do gabinete.

ESTRUTURA:
Possui formato retangular metálico, contendo
ventoinha, circuitos elétricos internos,
cabos que conectam com os  outros componentes
para fornecimento de energia.
''')

                elif opc == 7:
                    print(f'{'COOLERS':-^30}')
                    print('''
FUNÇÃO:
Responsáveis pelo resfriamento do computador.

LOCALIZAÇÃO:
Podem ficar no processador, gabinete e placa
de vídeo.

ESTRUTURA:
São compostos por ventoinhas que movimentam
o ar para reduzir a temperatura das peças.
''')

                elif opc == 8:
                    print(f'{'GABINETE':-^30}')
                    print('''
    
FUNÇÃO:
Responsável por proteger e organizar todas
as peças do computador.

LOCALIZAÇÃO:
É a estrutura externa do computador.

ESTRUTURA:
Possui formato de caixa metálica com espaço
interno para instalação dos componentes,
coolers e passagem de cabos.
''')

                elif opc == 9:
                    print('Voltando', end='')
                    for i in range(0,2):
                        sleep(0.5)
                        print('.', end='')
                    sleep(0.5)
                    print()
                    break

            except ValueError:
                print('Use apenas as opções existentes', end='')
                print()

            back = input('Voltar (ENTER)')
            while len(back) != 0:
                back = input('Voltar (ENTER)')
            else:
                continue

    elif res == 4:
        while True:
            print(f'{'TABUADA':-^20}')
            while True:
                nun = input('Número: ')
                if not nun.isdigit() or len(nun) == 0:
                    print('Apenas números..')
                    continue
                nun = int(nun)
                for i in range(1,11):
                    print(f'{nun} x {i} = {nun * i}')
                per = input('Deseja continuar? [S/N] ').upper().strip()
                while per not in 'SN' or len(per) == 0:
                    per = input('Deseja continuar? [S/N] ').upper().strip()
                if per == 'S':
                    continue
                elif per == 'N':
                    break
            break


    elif res == 5:
        print('Obrigado por usar meu programa!')
        sleep(3)
        break
