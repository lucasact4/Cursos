# Faça um programa que tenha uma FUNÇÃO chamada ESCREVA(),
# que receba um texto qualquer como PARÂMETRO e mostre
# uma mensagem com tamanho adaptável.
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~~~~~
print('=-'*15)


# Definição de Função
def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


# Programa Principal
mensagem = str(input('Digite uma aviso: '))
escreva(mensagem)
print('=-'*15)
