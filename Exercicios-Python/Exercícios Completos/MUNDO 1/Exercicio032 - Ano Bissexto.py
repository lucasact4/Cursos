# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
print('=-'*15)
from datetime import date
print('Digite o número 0 para analisar o ano atual !')
ano = int(input('Digite o ano que deseja descobrir se é BISSEXTO: '))
if ano == 0:
    ano = date.today().year
if (ano % 400 == 0) and (ano % 100 == 0):
    print('{} é um ano BISSEXTO !'.format(ano))
elif (ano % 4 == 0) and (ano % 100 != 0):
    print('{} é um ano BISSEXTO !'.format(ano))
else:
    print('{} não é um ano BISSEXTO !'.format(ano))
#BONUS +
print('-'*15)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano BISSEXTO !'.format(ano))
else:
    print('{} não é um ano BISSEXTO !'.format(ano))
print('=-'*15)
