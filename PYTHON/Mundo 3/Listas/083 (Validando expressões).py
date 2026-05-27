'''Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses. Seu aplicativo deverá analisar se a expressão
passada está com parênteses abetos e fechados na ordem correta.'''

pasta = []
#Minha resolução ↓
'''print('Digite uma expressão usando parênteses..')
per = input('Expressão: ')
pasta.append(per)

cont = 0
paren = False
valido = True
for p in pasta:
    for letra in p:
        if letra == '(':
            cont += 1
            paren = True
        elif letra == ')':
            cont -= 1
            paren = True

        if cont < 0:
            valido = False
            break

if cont == 0 and paren and per not in '()' and valido:
    print('Expressão válida!')
else:
    print('Expressão inválida!')'''

expr = str(input('Digite a Expressão: '))
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua Expressão esta válida!')
else:
    print('Sua Expressão esta errada!')