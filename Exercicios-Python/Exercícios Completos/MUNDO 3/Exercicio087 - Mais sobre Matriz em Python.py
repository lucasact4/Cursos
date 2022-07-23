# Aprimore o DESAFIO ANTERIOR, mostrando no final:
# A) A SOMA de todos os VALORES PARES digitados.
# B) A SOMA dos valores da TERCEIRA COLUNA.
# C) O MAIOR valor da SEGUNDA LINHA.
print('=-'*15)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos valores pares é {spar}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
print('=-'*15)
