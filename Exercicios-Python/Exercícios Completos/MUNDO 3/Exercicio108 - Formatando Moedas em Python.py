# Adapte o código do DESAFIO 107, criando uma função adicional chamada MOEDA()
# que consiga mostrar os valores como um valor monetário formatado.
from modules import moeda2
print('=-'*15)
var = float(input('Digite o preço: R$'))
print(f'A metade de {moeda2.moeda(var)} é {moeda2.moeda(moeda2.metade(var))}.')
print(f'O dobro de {moeda2.moeda(var)} é {moeda2.moeda(moeda2.dobro(var))}.')
print(f'Aumentando 10%, temos {moeda2.moeda(moeda2.aumentar(var))}.')
print(f'Diminuindo 10%, temos {moeda2.moeda(moeda2.diminuir(var))}.')
print('=-'*15)
