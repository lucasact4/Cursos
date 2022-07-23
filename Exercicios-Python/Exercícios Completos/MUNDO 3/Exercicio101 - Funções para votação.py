# Crie um programa que tenha uma FUNÇÃO chamada VOTO() que vai receber como PARÂMETRO o ANO DE NASCIMENTO
# de uma pessoa, RETORNANDO um valor LITERAL indicando se uma pessoa tem voto
# NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
print('=-' * 15)


def voto(a):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
print('=-' * 15)
