teste = []
teste.append('Vinicius')
teste.append(23)
galera = []
galera.append(teste[:])
teste[0]= 'Gustavo'
teste[1]= 40
galera.append(teste[:])
print(galera)
print(teste)