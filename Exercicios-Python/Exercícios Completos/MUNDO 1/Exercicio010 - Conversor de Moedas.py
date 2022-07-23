# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$3,27
print('=-'*15)
d = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${:.2f} você consegue comprar US${:.2f} Dólares.'.format(d, (d/3.27)))
print('=-'*15)
