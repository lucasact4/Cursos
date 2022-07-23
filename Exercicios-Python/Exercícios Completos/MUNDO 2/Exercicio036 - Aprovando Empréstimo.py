# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que não pode exceder 30% do salário ou então o empréstimo será negado.
print('=-'*15)
nome = str(input('Bem-vindo ao empréstimos rápidos !\nPara iniciarmos digite o seu nome: '))
valorc = float(input(f'Qual é o valor da casa Sr. {nome} ? R$'))
salario = float(input(f'Qual é o valor do seu salário Sr. {nome} ? R$'))
anos = int(input(f'Em quantos anos você deseja pagar o financiamento da casa Sr. {nome} ? '))
anos = anos * 12
pres = valorc / anos
pag = (salario / 100) * 30
if pres > pag:
    print(f'Prestação: {pres:.2f}\nDesculpe-nos Sr. {nome}!\n'
          'A prestação excedeu 30% do valor do seu salário', end='')
    print('e não podemos financiar a casa para você !')
else:
    print(f'Parabéns Sr. {nome}! Conseguimos financiar a casa para você !\nPrestação mensal: {pres:.2f}')
print('=-'*15)
