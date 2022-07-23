# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
print('=-'*15)
veloc = float(input('Informe a velocidade que o carro percorreu em Km/h: '))
if veloc > 80:
    print('Você foi multado !')
    veloc2 = (veloc - 80) * 7
    print('Você irá pagar um total de R${:.0f},00.'.format(veloc2))
else:
    print('Você não foi multado !')
print('=-'*15)
