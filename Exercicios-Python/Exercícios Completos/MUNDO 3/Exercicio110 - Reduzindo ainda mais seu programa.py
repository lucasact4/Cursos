# Adicione ao módulo MOEDA.PY criado nos desafios anteriores, uma função chamada RESUMO(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
from modules import moeda4
print('=-'*15)
var = float(input('Digite o preço: R$'))
moeda4.resumo(var, 10, 10)
print('=-'*15)
