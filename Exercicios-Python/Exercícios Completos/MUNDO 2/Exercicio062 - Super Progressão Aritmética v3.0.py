# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 TERMOS.
print('=-'*15)
print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
contador = 11
perg = 1
cont = 10
# OU décimo = termo + (10 - 1) * razão
# E for c in range(termo, "décimo + razão", razão):
while contador != 1:
    print(f'{termo}', end='→ ')
    termo = termo + razão
    contador = contador - 1
print('PAUSA')
while True:
    perg = int(input('Quantos termos você quer mostrar a mais? '))
    cont += perg
    if perg == 0:
        break
    perg2 = perg
    while perg2 != 0:
        print(f'{termo}', end='→ ')
        termo = termo + razão
        perg2 = perg2 - 1
    print('PAUSA')
print(f'Progressão finalizada com {cont} termos mostrados.')
print('=-'*15)
