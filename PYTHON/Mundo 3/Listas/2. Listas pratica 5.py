galera = [['Claudia', 28],['Vinicius', 23],['Marcelito', 10]]
print(galera)
for pessoa in galera:
    print(f'{pessoa[0]} idade {pessoa[1]}')

pessoa = []
dado = list()
for i in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoa.append(dado[:])
    dado.clear()

print(pessoa)
print(dado)