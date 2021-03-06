"""
Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
"""


def maisdezporcento(preço=0, taxa=0):
    res = preço + (preço * taxa / 100)
    return res


def menosdezporcento(preço=0, taxa=0):
    res = preço - (preço * taxa / 100)
    return res


def dobro(preço=0):
    res = preço * 2
    return res


def metade(preço=0):
    res = preço / 2
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')
