"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""


def aumentar(preço=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determinado preço.
    :param preço: o preço que se quer reajustar.
    :param taxa: qual a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?!
    :return: o valor reajustado, com ou sem formatação.
    '''
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    '''
       -> Calcula a diminuição de um determinado preço.
       :param preço: o preço que se quer reajustar.
       :param taxa: qual a porcentagem que será decrementada.
       :param formato: quer a saída formatada ou não?!
       :return: o valor reajustado, com ou sem formatação.
    '''
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    '''
          -> Calcula o dobro de um determinado preço.
          :param preço: o preço que se quer reajustar.
          :param formato: quer a saída formatada ou não?!
          :return: o valor dobrado, com ou sem formatação.
    '''
    res = preço * 2
    return res if not formato else moeda(res)

def metade(preço=0, formato=False):
    '''
            -> Calcula a metade de um determinado preço.
            :param preço: o preço que se quer reajustar.
            :param formato: quer a saída formatada ou não?!
            :return: a metade do preço original, com ou sem formatação.
      '''
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
