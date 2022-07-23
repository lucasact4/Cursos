# Faça um programa que tenha uma FUNÇÃO chamada ÁREA(),
# que receba as dimensões de um terreno retangular (LARGURA e COMPRIMENTO)
# e mostre a ÁREA DO TERRENO.
print('=-' * 15)


# Definição de Função
def area(larg, comp):
    print(f'A área de um terreno {larg}x{comp} é de {larg * comp}m².')


# Programa Principal
print(' Controle de Terrenos\n', '-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
print('=-' * 15)
