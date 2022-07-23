# Crie um programa que leia o NOME e o PREÇO de VÁRIOS PRODUTOS.
# O programa deverá perguntar se o USUÁRIO vai continuar.
# No final, mostre:
# A) Qual é o TOTAL GASTO na compra.
# B) Quantos produtos custam MAIS de R$1000.
# C) Qual é o NOME do produto mais BARATO.
print('=-'*15)
cont = 1
tot = 0
quant = 0
barato = 0
nbarato = ''
while True:
    print(f'----- {cont}ª PRODUTO -----')
    nome = str(input('Nome: '))
    preço = int(input('Preço: R$'))
    tot += preço
    if preço > 1000:
        quant += 1
    if cont == 1:
        barato = preço
    else:
        if preço < barato:
            barato = preço
            nbarato = nome
    while True:
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if continuar != 'S' and continuar != 'N':
            print('Opção inválida! Tente novamente com (S - Sim | N - Não)!')
        else:
            break
    cont += 1
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${tot:.2f}\nTemos {quant} produtos custando mais de R$1000.00\nO produto mais barato foi a(o) Lapiseira que custa R${barato:.2f}')
print('=-'*15)
