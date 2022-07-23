def aumentar(var=0):
    var = (var * 10 / 100) + var
    return var


def diminuir(var=0):
    var = var * 90 / 100
    return var


def dobro(var=0):
    return var * 2


def metade(var=0):
    return var / 2


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
