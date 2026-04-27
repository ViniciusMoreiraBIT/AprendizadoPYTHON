'''Crie um programa que tenha uma tupla totalmente penchida
com uma contagem por extenso, de 0 até 20.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
mostrá-lo por extenso.'''


#Minha resolução ↓
'''num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
res = int(input('Digite um número de 0 e 20: '))
while res < 0 or res > 20:
    res = int(input('ERRO..Digite um número de 0 e 20: '))
print(f'Você digitou o número {num[res]}')'''

cont = ('zero','um','dois','três','quatro','cinco',
       'seis','sete','oito','nove','dez','onze',
       'doze','treze','quatorze','quinze','dezesseis',
       'dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}')
        per = input('Quer novamente [S/N]: ').upper().strip()[0]
        while per not in 'NS':
            per = input('Quer novamente [S/N]: ').upper().strip()[0]
        if per == 'N':
            break
        elif per == 'S':
            continue
    print('Tente novamente.',end='')

