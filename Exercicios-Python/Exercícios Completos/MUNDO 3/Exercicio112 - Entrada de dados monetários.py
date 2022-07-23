# Dentro do pacote UTILIZADESCEV que criamos no DESAFIO 111, temos um MÓDULO chamado DADO.
# Crie uma função chamada LEIADINHEIRO() que seja capaz de funcionar como a função INPUT(),
# mas com uma VALIDAÇÃO DE DADOS para aceitar apenas valores que sejam MONETÁRIOS.
from modules.utilidadescev import moeda, dado
print('=-'*15)
p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)
print('=-'*15)
