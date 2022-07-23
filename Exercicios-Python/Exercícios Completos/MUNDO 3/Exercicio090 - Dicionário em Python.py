# Faça um programa que leia NOME E MÉDIA de um aluno, guardando também a SITUAÇÃO em um DICIONÁRIO.
# No final, mostre o conteúdo da estrutura na tela.
print('=-'*15)
dicio = dict()
dicio['nome'] = str(input('Nome: '))
dicio['media'] = float(input('Média: '))
for k, v in dicio.items():
    print(f'- {k} é igual a {v}')
print('- situação é igual a ', end='')
if dicio['media'] < 5:
    print('Reprovado')
elif dicio['media'] < 7:
    print('Recuperação')
else:
    print('Aprovado')
print('=-'*15)