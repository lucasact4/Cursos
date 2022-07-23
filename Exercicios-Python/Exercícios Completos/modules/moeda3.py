def aumentar(var=0, formato=False):
    var = (var * 10 / 100) + var
    return var if formato is False else moeda(var)


def diminuir(var=0, formato=False):
    var = var * 90 / 100
    return var if formato is False else moeda(var)


def dobro(var=0, formato=False):
    var *= 2
    return var if not formato else moeda(var)


def metade(var=0, formato=False):
    var /= 2
    return var if not formato else moeda(var)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
