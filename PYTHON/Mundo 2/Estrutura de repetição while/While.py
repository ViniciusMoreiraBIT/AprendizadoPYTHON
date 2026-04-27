n = 1
loop = 1
par = impar = 0
while n != 0:
    n = int(input(f'{loop}º Número: '))
    loop += 1
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'{par} números pares\n{impar} números impares')