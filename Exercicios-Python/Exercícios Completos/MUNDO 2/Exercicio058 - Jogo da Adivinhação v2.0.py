# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um NÚMERO ENTRE 0 E 10.
# Só que agora o jogador vai adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
print('=-'*15)
from random import randint
from time import sleep
num1 = randint(0, 10)
cont = 1
print('O computador está pensando em um número aleátorio de 0 a 10...')
num2 = int(input('Para brincar, digite um número de 0 a 10: '))
print('PROCESSANDO...')
sleep(1)
while num2 > 10 or num2 < 0:
    num2 = int(input('Número fora de opção!\nTente novamente com números de 0 a 10: '))
    print('PROCESSANDO...')
    sleep(1)
while num1 != num2:
    num2 = int(input('Que pena! Você errou! :(\nTente novamente com números de 0 a 10: '))
    while num2 > 10 or num2 < 0:
        num2 = int(input('Número fora de opção!\nTente novamente com números de 0 a 10: '))
        print('PROCESSANDO...')
        sleep(1)
    cont += 1
    print('PROCESSANDO...')
    sleep(1)
print(f'Parabéns ! Você acertou ! :)\nO número correto é {num1} e foram {cont} palpites ao total para acertar!')
print('=-'*15)
