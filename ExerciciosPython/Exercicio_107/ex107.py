"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""


def MaisDezPorCento(valor):
    aumento = valor * 0.1
    print(f'Aumentando 10%, temos R${aumento + valor}')


def MenosDezPorCento(valor):
    aumento = valor * 0.1
    print(f'Diminuindo 10%, temos R${aumento - valor}')


def Dobro(valor):
    dobro = valor * 2
    print(f'O dobro de R${valor} é R${dobro}')


def Metade(valor):
    metade = valor / 2
    print(f'A metade de R${valor} é R${metade}')
