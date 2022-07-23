# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# Considerando a maioridade com 21 anos.
print('=-'*15)
from datetime import date
anoatual = date.today().year
maior = []
menor = []
for x in range(1, 8):
    p = int(input(f'Digite o ano de nascimento da {x}º pessoa: '))
    p = anoatual - p
    if p >= 21:
        maior.append(p)
    else:
        menor.append(p)
print(f'Total de pessoas com maioridade atingida: {len(maior)}\nTotal de pessoas que ainda não atingiram a maioridade: {len(menor)}')
print('=-'*15)
