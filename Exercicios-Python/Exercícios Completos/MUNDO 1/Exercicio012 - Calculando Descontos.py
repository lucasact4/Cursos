# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
print('=-'*15)
p = float(input('Digite o preço do produto que deseja comprar R$'))
d = p*5/100
print('Parabéns! Você ganhou um desconto de 5% ! e o seu novo preço é R${}.'.format(p-d))
print('=-'*15)
