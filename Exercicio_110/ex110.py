"""
Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""


def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)

def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

def resumo(preço = 0, taxaAu = 10, taxaRe = 5):
    print('\033[1;31m-\033[m'*30)
    print('RESUMO DO VALOR'.center(30))
    print('\033[1;31m-\033[m'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço,True)}')
    print(f'Com {taxaAu}% de aumento: {aumentar(preço,taxaAu,True)}')
    print(f'Com {taxaRe}% de redução: \t{diminuir(preço,taxaRe,True)}')
    print('\033[1;31m-\033[m'*30)
