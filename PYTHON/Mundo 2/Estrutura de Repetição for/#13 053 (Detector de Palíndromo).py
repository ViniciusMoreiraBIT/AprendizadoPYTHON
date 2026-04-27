'''Crie um programa que leia uma frase
qualquer e diga se ela é um palindromo,
desconsiderando os espaços
EX: Apos a sopa
A sacada da casa
A torre da derrota
O lobo Ama bolo'''

'''p = input('Frase: ').strip().upper()
#inverso= p.lower().replace(' ','')[::-1]
#normal= p.lower().replace(' ','')
if p.replace(' ','')[::-1] == p.replace(' ',''):
    print('É um Palindromo!')
    print(p.replace(' ',''), p[::-1].replace(' ',''))
else:
    print('Negativo')'''

p = input('Frase: ').strip().upper()
palavras = p.split() #separou cada palavra em uma lista
junto=''.join(palavras) #Juntou as palavras (sem espaços)
inverso = ''
for i in range(len(junto) - 1, -1, -1):
    print(junto[i], i) #pra entender melhor
    inverso += junto[i]
print(junto, inverso)
if inverso ==  junto:
    print('É um Palindromo!')
else:
    print('Negativo!')
