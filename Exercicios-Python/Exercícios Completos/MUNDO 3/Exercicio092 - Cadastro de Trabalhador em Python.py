# Crie um programa que leia NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALHO
# e cadastre-os (com IDADE) em um dicionário se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ANO DE CONTRATAÇÃO e o SALÁRIO.
# Calcule e acrescente, além da IDADE, com quantos anos a pessoa vai se APOSENTAR.
print('=-'*15)
from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
    print('-' * 20)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
print('=-'*15)
