# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
print('=-'*15)
print('{:=^40}'.format('LOJAS ACT4'))
valor = float(input('Digite o valor do produto: R$'))
escolha = int(input('''Formas de pagamento:
[ 1 ] À vista dinheiro/cheque: 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto
[ 3 ] Em até 2x no cartão: preço normal
[ 4 ] 3x ou mais no cartão: 20% de juros
Escolha a forma de pagamento de acordo com a sua numeração: '''))
while escolha != 4 and escolha != 3 and escolha != 2 and escolha != 1:
    escolha = int(input('Opção Incorreta! Tente novamente!\nEscolha a forma de pagamento de acordo com as numerações disponíveis: '))
if escolha == 1:
    vistad = valor - (valor / 100) * 10
    print(f'Novo preço: {vistad:.2f}')
elif escolha == 2:
    vistac = valor - (valor / 100) * 5
    print(f'Novo preço: {vistac:.2f}')
elif escolha == 3:
    print(f'Sua compra será parcelada em 2x de R${valor/2:.2f} SEM JUROS.\nMesmo preço: {valor:.2f}')
else:
    par = int(input('Quantas parcelas? '))
    cartao = valor + (valor / 100) * 20
    print(f'Sua compra será parcelada em {par}x de R${cartao/par:.2f} COM JUROS.\nNovo preço: {cartao:.2f}')
print('=-'*15)
