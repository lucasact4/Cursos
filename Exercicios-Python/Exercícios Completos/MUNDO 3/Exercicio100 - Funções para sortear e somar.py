# Faça um programa que tenha uma LISTA chamada NÚMEROS e duas FUNÇÕES chamadas SORTEIA()
# e SOMAPAR(). A primeira função vai sortear 5 NÚMEROS e vai colocá-los dentro da lista
# e a segunda função vai mostrar a SOMA entre todos os valores PARES sorteados
# pela função anterior.
print('=-'*15)
from random import randint
from time import sleep


# Definição de Função
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for x in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somapar():
    soma = 0
    for y in numeros:
        if y % 2 == 0:
            soma += y
    print(f'Somando os valores pares de {numeros}, temos {soma}')


# Programa Principal
numeros = []
sorteia(numeros)
somapar()
print('=-'*15)