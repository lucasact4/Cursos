# Faça um programa que tenha uma FUNÇÃO chamada CONTADOR(),
# que receba três PARÂMETROS: INÍCIO, FIM e PASSO e realize a contagem.
# Seu programa tem que realizar TRÊS CONTAGENS através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem PERSONALIZADA.
print('=-'*15)
from time import sleep


# Definição de Função
def linha():
    print('-' * 20)
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= p
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
linha()
print('=-'*15)
