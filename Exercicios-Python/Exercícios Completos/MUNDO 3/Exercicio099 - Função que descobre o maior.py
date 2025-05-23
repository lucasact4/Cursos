# Faça um programa que tenha uma FUNÇÃO chamada MAIOR(),
# que receba vários PARÂMETROS com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o MAIOR.
print('=-'*15)
from time import sleep


# Definição de Função
def maior(* num):
    cont = maior = 0
    print('-' * 20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print('=-'*15)
