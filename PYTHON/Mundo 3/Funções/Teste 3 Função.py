valores = [7,4,2,3,2,1]

def dobra(ll):
    cont = 0
    while cont < len(ll):
        ll[cont] *= 2
        cont += 1
    print(valores)


def quebrar(msg):
    for i in msg:
        print(i, end=' ')

print(valores) # lista original
dobra(valores) # Muda a lista principal
print(valores) # lista nova
quebrar(valores)