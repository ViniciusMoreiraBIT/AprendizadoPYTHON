soma = 0
while True:
    n = int(input('N: '))
    if n == 999:
        break
    soma += n
print(f'A soma vale {soma}')