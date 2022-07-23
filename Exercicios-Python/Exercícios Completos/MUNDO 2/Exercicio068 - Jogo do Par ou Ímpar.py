# Faça um programa que jogue PAR OU ÍMPAR com o computador.
# O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
print('=-'*15)
from random import randint
print('-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-'*15)
comp = randint(1, 10)
errou = False
cont = 0
pi = ' '
while not errou:
    num = int(input('Diga um valor: '))
    desc = comp + num
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    if pi == 'P' and desc % 2 == 0:
        print('-'*10)
        print(f'Você jogou {num} e o computador {comp}. Total de {desc} DEU PAR')
        print('-'*10)
        print('Você VENCEU!\nVamos jogar novamente...')
        print('-'*15)
        cont += 1
    elif pi == 'I' and desc % 2 == 1:
        print('-'*10)
        print(f'Você jogou {num} e o computador {comp}. Total de {desc} DEU ÍMPAR')
        print('-'*10)
        print('Você VENCEU!\nVamos jogar novamente...')
        print('-'*15)
        cont += 1
    elif pi == 'I' and desc % 2 == 0:
        print('-'*10)
        print(f'Você jogou {num} e o computador {comp}. Total de {desc} DEU PAR')
        print('-'*10)
        print('Você PERDEU!')
        print('-'*15)
        errou = True
    else:
        print('-'*10)
        print(f'Você jogou {num} e o computador {comp}. Total de {desc} DEU ÍMPAR')
        print('-'*10)
        print('Você PERDEU!')
        print('-'*15)
    comp = randint(1, 10)
print(f'GAME OVER! Você venceu {cont} vezes.')
print('=-'*15)
