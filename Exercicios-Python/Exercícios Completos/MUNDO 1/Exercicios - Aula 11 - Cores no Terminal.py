# Bonus de:
# Cores no Terminal
print('=-'*15)
# Ex 1
print('\033[1;31;46mOlá, Mundo!\033[m')
print('-'*15)
# Ex 2
nome = 'Lucas'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;32m', nome, '\033[m'))
print('-'*15)
# Ex 3
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))
print('-'*15)
# Ex 3
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
print('=-'*15)
# Importações de Bibliotecas
import math
numero = 5
print('Arredonda para Cima')
print(math.ceil(numero))
print('-'*15)
print('Arredonda para Baixo')
print(math.floor(numero))
print('-'*15)
print('Retira os números depois da vírgula ou ponto')
print(math.trunc(numero))
print('-'*15)
print('Calcula a Raiz Quadrada')
print(math.sqrt(numero))
print('-'*15)
print('Calcula o fatorial de um número')
print(math.factorial(numero))
print('-'*15)
print('Exponenciação do número')
print(math.pow(5, 5))
print('=-'*15)
# Importações de Bibliotecas Externas
import emoji
# https://pypi.org/project/emoji/
print(emoji.emojize("Olá ! Mundo ! :globo_mostrando_as_américas:", language='pt'))
# Transformação de Texto
frase = 'Programação é D+'
print(frase.replace('D+', 'Demais'))
# Estrutura Condicional Simplificada
preço1 = 50
# Se o preço1 for menor ou igual a 100 será multiplicado 2 vezes, caso ao contrário, será multiplicado 4 vezes
preço2 = preço1 * 2 if preço1 <= 100 else preço1 * 4
print(preço2)
print('=-'*15)
