# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('=-'*15)
print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = razão * 10 + termo
# OU décimo = termo + (10 - 1) * razão
# E for c in range(termo, "décimo + razão", razão):
for c in range(termo, cont, razão):
    print(f'{c}', end='→ ')
print('ACABOU')
print('=-'*15)
