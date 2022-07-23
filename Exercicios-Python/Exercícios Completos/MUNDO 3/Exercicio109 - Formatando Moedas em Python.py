# Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem UM PARÂMETRO a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função MOEDA(), desenvolvida no DESAFIO 108.
from modules import moeda3
print('=-'*15)
var = float(input('Digite o preço: R$'))
print(f'A metade de {moeda3.moeda(var)} é {moeda3.metade(var, True)}.')
print(f'O dobro de {moeda3.moeda(var)} é {moeda3.dobro(var, True)}.')
print(f'Aumentando 10%, temos {moeda3.aumentar(var, True)}.')
print(f'Diminuindo 10%, temos {moeda3.diminuir(var, True)}.')
print('=-'*15)
