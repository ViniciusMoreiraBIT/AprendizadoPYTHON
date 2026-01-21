'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela:
-Abaixo de 18.5: Abaixo do Peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

peso = float(input('Seu peso: '))
altura= float(input('Sua altura: '))
IMC = peso / (altura * altura)
if IMC < 18.5:
    print(f'IMC: {IMC:.2f}')
    print('Abaixo do Peso')
elif IMC < 25:
    print(f'IMC: {IMC:.2f}')
    print('Peso Ideal')
elif IMC < 30:
    print(f'IMC: {IMC:.2f}')
    print('Sobrepeso')
elif IMC <= 40:
    print(f'IMC: {IMC:.2f}')
    print('Obesidade')
elif IMC > 40:
    print(f'IMC: {IMC:.2f}')
    print('Obesidade Mórbida')