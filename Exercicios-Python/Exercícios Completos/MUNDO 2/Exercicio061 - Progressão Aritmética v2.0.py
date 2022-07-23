# Refaça o DESAFIO 051, lendo o PRIMEIRO TERMO e a RAZÃO de uma PA,
# mostrando os 10 PRIMEIROS TERMOS da progressão usando a estrutura while.
print('=-'*15)
print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
contador = 11
# OU décimo = termo + (10 - 1) * razão
# E for c in range(termo, "décimo + razão", razão):
while contador != 1:
    print(f'{termo}', end='→ ')
    termo = termo + razão
    contador = contador - 1
print('ACABOU')
print('=-'*15)
