# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
print('=-'*15)
from random import randint
from time import sleep
num1 = randint(0, 5)
print('O computador está pensando em um número aleátorio de 0 a 5...')
num2 = int(input('Para brincar, digite um número de 0 a 5 para descobrir se você acertou: '))
print('PROCESSANDO...')
sleep(1)
if num2 == num1:
    print('Parabéns ! Você acertou ! :)\nO número correto é:', num1)
else:
    print('Que pena ! Você errou ! :(\nO número correto é:', num1)
print('=-'*15)
