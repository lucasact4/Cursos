# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
print('=-'*15)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'REPROVADO.\nNota: {media:.1f}')
elif 7 > media >= 5:
    print(f'RECUPERAÇÃO.\nNota: {media:.1f}')
else:
    print(f'APROVADO.\nNota: {media:.1f}')
print('=-'*15)
