# Crie um PACOTE chamado UTILIDADESCEV que tenha dois MÓDULOS INTERNOS chamados MOEDA e DADO.
# Transfira todas as funções utilizadas nos DESAFIOS 107, 108 e 109
# para o primeiro pacote e mantenha tudo funcionando.
from modules.utilidadescev import moeda
print('=-'*15)
var = float(input('Digite o preço: R$'))
moeda.resumo(var, 35, 22)
print('=-'*15)
