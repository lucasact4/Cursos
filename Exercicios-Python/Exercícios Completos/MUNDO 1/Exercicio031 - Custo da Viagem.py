# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
print('=-'*15)
viagem = int(input('Digite a distância de uma viagem em Km: '))
if viagem <= 200:
    preco = viagem * 0.5
else:
    preco = viagem * 0.45
print('A distância da sua viagem é {}Km e você irá pagar um total de R${:.2f}.'.format(viagem, preco))
print('-'*15)
preco2 = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('A distância da sua viagem é {}Km e você irá pagar um total de R${:.2f}.'.format(viagem, preco2))
print('=-'*15)
