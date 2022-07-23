# Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
print('=-'*15)
sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Opção Incorreta!\nTente novamente com (M - Masculino | F - Feminino)!\nDigite o seu sexo [M/F]: ')).upper().strip()
if sexo == 'M':
    print('Sexo Masculino escolhido com sucesso!')
if sexo == 'F':
    print('Sexo Feminino escolhido com sucesso!')
print('=-'*15)
