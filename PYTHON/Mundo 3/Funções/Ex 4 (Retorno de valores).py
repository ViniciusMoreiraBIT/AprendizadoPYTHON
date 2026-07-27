def somar(a=0,b=0,c=0):
    soma = a + b + c
    #print(soma) → não retorna nenhum valor, apenas o print
    return soma

r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(6)
print(f'Meus cálculos deram: {r1}, {r2} e {r3}')