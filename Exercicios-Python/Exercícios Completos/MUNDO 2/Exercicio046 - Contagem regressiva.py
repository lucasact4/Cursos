# Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o
# estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
print('=-'*15)
from time import sleep
for x in range(10, -1, -1):
    print(f'Contagem Regressiva para virada do ano: {x}')
    if x == 0:
        break
    sleep(1)
print('Feliz Ano Novo!!!')
print('=-'*15)
