# Faça um programa que ajude um jogador da MEGA SENA a criar PALPITES.
# O programa vai perguntar QUANTOS JOGOS serão gerados e vai sortear
# 6 NÚMEROS ENTRE 1 E 60 para cada jogo, cadastrando tudo em uma LISTA COMPOSTA.
print('=-'*15)
from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 25)
print(f'{"JOGA NA MEGA SENA":^25}')
print('-' * 25)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-' * 3, f'SORTEANDO {quant} JOGOS ', '-' * 3)
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
sleep(1)
print('-' * 5, '| BOA SORTE! |', '-' * 5)
print('=-'*15)
