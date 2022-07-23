# Crie um programa que crie uma MATRIZ de DIMENSÃO 3X3 e preencha com valores lidos pelo teclado.
# ⬜ ⬜ ⬜
# ⬜ ⬜ ⬜
# ⬜ ⬜ ⬜
# No final, mostre a MATRIZ na tela, com a formatação correta.
print('=-'*15)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-'*15)
