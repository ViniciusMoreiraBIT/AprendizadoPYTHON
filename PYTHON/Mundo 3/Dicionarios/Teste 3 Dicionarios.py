estado = dict()
brasil = list()
for cont in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil: #em cada item da LISTA
    for u, s in e.items(): # em cada uf e sigla do dicionário de cada item da lista
        print(f'{u} = {s}')

        # LISTA
        # brasil
        # │
        # ├── DICIONÁRIO 1
        # │     ├── uf = Paraná (u = s) (chave = valor)
        # │     └── sigla = PR  (u = s)
        # │
        # ├── DICIONÁRIO 2
        # │     ├── uf = São Paulo (u = s)
        # │     └── sigla = SP (u = s)
        # │
        # └── DICIONÁRIO 3
                # ├── uf = Rio (u = s)
                # └── sigla = RJ (u = s)

for e in brasil:
    for v in e.values():
        print(v)
        # Paraná
        # PR
        # São Paulo
        # SP

for e in brasil:
    for u in e.keys():
        print(u)
        # uf
        # sigla
        # uf
        # sigla
