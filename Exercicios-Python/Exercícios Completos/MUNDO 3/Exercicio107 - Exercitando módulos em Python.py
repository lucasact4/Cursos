# Crie um módulo chamado moeda1.py que tenha as funções incorporadas AUMENTAR(), DIMINUIR(), DOBRO() e METADE().
# Faça também um programa que IMPORTE esse módulo e use algumas dessas funções.
from modules import moeda1
print('=-'*15)
var = float(input('Digite o preço: R$'))
print(f'A metade de R${var} é R${moeda1.metade(var)}.')
print(f'O dobro de R${var} é R${moeda1.dobro(var)}.')
print(f'Aumentando 10%, temos R${moeda1.aumentar(var)}.')
print(f'Diminuindo 10%, temos R${moeda1.diminuir(var)}.')
print('=-'*15)
