bilhetes = {
    "Bilhete 1 - A": [2, 22, 30, 36, 38, 42, 59],
    "Bilhete 1 - B": [9, 11, 31, 32, 35, 49, 50],
    "Bilhete 1 - C": [1, 31, 37, 39, 43, 57, 58],
    "Bilhete 1 - D": [1, 14, 17, 19, 32, 38, 60],
    "Bilhete 1 - E": [2, 11, 12, 22, 41, 42, 44],
    "Bilhete 1 - F": [10, 33, 35, 44, 49, 50, 53],
    "Bilhete 1 - G": [4, 20, 29, 39, 53, 54, 59],

    "Bilhete 2 - A": [10, 17, 18, 20, 50, 54, 59],
    "Bilhete 2 - B": [6, 15, 27, 30, 31, 42, 59],
    "Bilhete 2 - C": [15, 19, 30, 36, 40, 46, 51],
    "Bilhete 2 - D": [3, 17, 25, 27, 33, 35, 53],
    "Bilhete 2 - E": [14, 22, 25, 27, 33, 37, 48],
    "Bilhete 2 - F": [1, 5, 7, 10, 22, 26, 35],
    "Bilhete 2 - G": [16, 27, 31, 44, 48, 57, 60]
}

# =========================
# Entrada dos números sorteados
# =========================

resultado = []

print('=' * 40)
print('DIGITE OS 6 NÚMEROS SORTEADOS')
print('=' * 40)

for i in range(6):
    numero = int(input(f'{i+1}º número: '))
    resultado.append(numero)

# =========================
# Conferência
# =========================

print('\n' + '=' * 40)
print('RESULTADO DOS JOGOS')
print('=' * 40)

for nome, jogo in bilhetes.items():

    acertos = []

    for numero in jogo:
        if numero in resultado:
            acertos.append(numero)

    print(f'\n{nome}')
    print(f'Números do jogo: {jogo}')
    print(f'Acertos: {len(acertos)} -> {acertos}')

    # Premiação
    if len(acertos) == 6:
        print('>>> SENA!')
    elif len(acertos) == 5:
        print('>>> QUINA!')
    elif len(acertos) == 4:
        print('>>> QUADRA!')