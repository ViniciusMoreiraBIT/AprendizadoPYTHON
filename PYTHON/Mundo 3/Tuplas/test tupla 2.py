a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5)) #Quantas vezes aparece o 5
print(c.index(8)) #Qual posição esta o 8 ?
print(c.index(5)) #Qaundo tem 2 numeros ele mostra a primeira ocorrencia
print(c.index(5, 2))#"mostre o 5 apartir da posição 2"

pessoa = ('Vinicius', 23, 'M', 76)
del pessoa #tupla pode apenas ser deletada
print(pessoa)