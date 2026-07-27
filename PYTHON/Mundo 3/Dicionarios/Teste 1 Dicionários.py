pessoas = {'nome':'Vinicius','sexo':'M','idade': 23}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos!')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.values():
    print(k, end=' ')
print()
for k in pessoas.keys():
    print(k, end=' ')
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
pessoas['nome'] = 'Claudia'
pessoas['idade'] = 28
pessoas['altura'] = 1.69
print(pessoas)
