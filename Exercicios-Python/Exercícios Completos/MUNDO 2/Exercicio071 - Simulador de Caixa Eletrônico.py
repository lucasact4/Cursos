# Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO.
# No início, pergunte ao usuário qual será o VALOR A SER SACADO (número inteiro)
# e o programa vai informar quantas CÉDULAS de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('=-'*15)
print('='*15)
print('{:^15}'.format('BANCO ACT4'))
print('='*15)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=-'*15)
