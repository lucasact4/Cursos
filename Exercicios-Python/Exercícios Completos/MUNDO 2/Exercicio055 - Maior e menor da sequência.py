# Faça um programa que leia o peso de cinco pessoas. No final,
# mostre qual foi o maior e o menor peso lidos.
print('=-'*15)
pessoas = []
pesoma = 0
pesome = 0
for x in range(1, 6):
    p = float(input(f'Digite o peso da {x}º pessoa: '))
    if x == 1:
        pesoma = p
        pesome = p
    else:
        if p > pesoma:
            pesoma = p
        elif p < pesome:
            pesome = p
print(f'O maior peso lido foi {pesoma}Kg, já o menor foi {pesome}Kg!')
print('=-'*15)
