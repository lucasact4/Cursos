# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('=-'*15)
km = int(input('Quantos Km o carro percorreu ? '))
dias = int(input('Por quantos dias ele foi alugado ? '))
kmp = 0.15 * km
diasp = 60 * dias
print('O carro percorreu {}Km por {} dias e o custo total foi R${}.'.format(km, dias, kmp + diasp))
#BONUS +
pago = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${pago:.2f}.')
print('=-'*15)
