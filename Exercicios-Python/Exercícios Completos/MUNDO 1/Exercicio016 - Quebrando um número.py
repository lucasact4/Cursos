# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex: 
# Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.
print('=-'*15)
from math import floor, ceil, trunc
n = float(input('Digite um número: '))
print('O número {} tem a parte Inteira {}.'.format(n, trunc(n)))
#BONUS +
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, int(n)))
print('O número {} tem a parte Inteira {}.'.format(n, floor(n)))
print('O número {} tem seu arredondamento {}.'.format(n, ceil(n)))
print('=-'*15)
