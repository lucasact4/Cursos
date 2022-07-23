# Crie um programa que tenha uma FUNÇÃO FATORIAL() que receba dois parâmetros:
# O primeiro que indique o NÚMERO a calcular e o outro chamado SHOW,
# que será um valor LÓGICO (OPCIONAL) indicando se será mostrado ou não
# na tela o processo de cálculo do fatorial.
print('=-'*15)


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
print(fatorial(5, show=True))
print('=-'*15)
help(fatorial)
print('=-'*15)
