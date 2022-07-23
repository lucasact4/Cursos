# Faça um programa que tenha uma FUNÇÃO chamada FICHA(), que receba dois PARÂMETROS OPCIONAIS:
# o NOME de um jogador e quantos GOLS ele marcou.
# O programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que
# algum dado não tenha sido informado corretamente.
print('=-'*15)


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
print('=-'*15)
