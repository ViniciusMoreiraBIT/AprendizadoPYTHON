try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# except Exception as erro:
#     print(f'Infelizmente tivemos um problema. {erro.__class__}')
except KeyboardInterrupt:
    print('\nO usuário preferiu não informar os dados!')
except (ValueError, ValueError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir por 0!')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre, muito obrigado!')
