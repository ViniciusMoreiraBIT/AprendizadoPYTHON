def fatorial(num = 1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é: {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são: {f1}, {f2} e {f3}')