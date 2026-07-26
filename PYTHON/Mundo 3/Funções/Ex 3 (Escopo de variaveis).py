def teste(b):
    global a # A de dentro do escopo local passa a valer globalmente
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

# programa principal ↓
a = 5 # A global
print(f'A fora vale {a}')
teste(a)
print()

print(f'segundo A fora vale {a}')
teste(a) # segunda chamada com A global alterado dentro do escopo local
#print(c) → ERRO!, porque foi definido apenas no escopo local (def teste)