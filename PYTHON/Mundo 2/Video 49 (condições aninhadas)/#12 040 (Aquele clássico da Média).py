'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0: Reprovado
-Média entre 5.0 e 6.9: Recuperação
-Média 7.0 ou superior: Aprovado'''
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print(f'Reprovado! nota {round(media, 1)}') #round(valor, casas_decimais)... round(media, 1) = uma casa decimal
elif media <= 6.9:
    print(f'Recuperação! nota {round(media, 1)}')
elif media >= 7.0:
    print(f'Aprovado! nota {round(media, 1)}')
print('Bons estudos!')