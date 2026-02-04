from time import sleep
Pss = []

for i in range(0,2):
    print(f'{i + 1}º Cadastro:')
    while True:
        id=input('ID: ')
        if not id.isdigit(): #SE NÃO for só numero:
            print('ID invalido')
            continue
        else:
            break
    while True:
        nome=input('Nome: ')
        if not nome.isalpha(): #SE NÃO for só letras:
            continue
        else:
            break
    while True:
        idade=input('Idade: ')
        if not idade.isdigit(): #SE NÃO for só numero:
            continue
        else:
            break
    Pss.append({'Nome': nome, 'Idade': int(idade),'ID': int(id)})

def menu_nome():
    print(f'\nID Cadastrados: {Pss[0]['ID']} | {Pss[1]['ID']}\n')
    while True:
        ctt = input('ID do Contato:')
        if not ctt.isdigit() or int(ctt) not in (Pss[0]['ID'],Pss[1]['ID']):
            print('ERRO')
            continue
        elif int(ctt) == Pss[0]['ID']:
            print(f'\n{Pss[0]['Nome']}\n')
            break
        elif int(ctt) == Pss[1]['ID']:
            print(f'\n{Pss[1]['Nome']}\n')
            break
    while True:
        voltar=input('Pressione ENTER para sair')
        if voltar == '':
            print('Saindo', end='')
            for i in range(0,3):
                sleep(0.5)
                print('.', end='')
            break
        else:
            continue

def menu_idade():
    print(f'\nID Cadastrados: {Pss[0]['ID']} | {Pss[1]['ID']}\n')
    while True:
        res = input('ID do Contato: ')
        if not res.isdigit() or int(res) not in (Pss[0]['ID'],Pss[1]['ID']):
            print('ERRO')
            continue
        elif int(res) == Pss[0]['ID']:
            print(f'\n{Pss[0]['Idade']} Anos\n')
            break
        elif int(res) == Pss[1]['ID']:
            print(f'\n{Pss[1]['Idade']} Anos\n')
            break
        else:
            break
    while True:
        voltar=input('Pressione ENTER para sair')
        if voltar == '':
            print('Saindo', end='')
            for i in range(0,3):
                sleep(0.5)
                print('.', end='')
            break

def menu_ctt():
    print(f'\nId Cadastrados: {Pss[0]['ID']} | {Pss[1]['ID']}\n')
    while True:
        res = input('ID do Contato: ')
        if not res.isdigit() or int(res) not in (Pss[0]['ID'],Pss[1]['ID']):
            print('ERRO')
            continue
        elif int(res) == Pss[0]['ID']:
            print(f'\n{Pss[0]['Nome']}\n{Pss[0]['Idade']} Anos\n')
            break
        elif int(res) == Pss[1]['ID']:
            print(f'\n{Pss[1]['Nome']}\n{Pss[1]['Idade']} Anos\n')
            break
        else:
            break
    while True:
        voltar = input('Pressione ENTER para sair')
        if voltar == '':
            print('Saindo', end='')
            for i in range(0,3):
                sleep(0.5)
                print('.', end='')
            break

def menu():
    while True:
        print('=-'*5)
        print('VISUALIZAR:\n(1) NOME\n(2) IDADE\n(3) CONTATO geral\n(Enter) SAIR')
        print('=-' * 5)
        res = input('Opção: ')
        if res == '':
            print('.', end='')
            for i in range(0, 2):
                sleep(0.5)
                print('.', end='')
            sleep(0.5)
            break
        elif int(res) == 1:
            menu_nome()
        elif int(res) == 2:
            menu_idade()
        elif int(res) == 3:
            menu_ctt()
        else:
            continue

menu()


