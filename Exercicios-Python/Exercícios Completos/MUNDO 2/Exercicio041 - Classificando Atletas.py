# A Confederação Nacional de Natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER
print('=-'*15)
from datetime import date
nasc = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print(f'Classificação: MIRIM\nIdade: {idade}')
elif idade <= 14:
    print(f'Classificação: INFANTIL\nIdade: {idade}')
elif idade <= 19:
    print(f'Classificação: JUNIOR\nIdade: {idade}')
elif idade <= 25:
    print(f'Classificação: SÊNIOR\nIdade: {idade}')
else:
    print(f'Classificação: MASTER\nIdade: {idade}')
print('=-'*15)
