"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'Primeiro jogador': randint(1, 6),
    'Segundo jogador': randint(1, 6),
    'Terceiro jogador': randint(1, 6),
    'Quarto jogador': randint(1, 6)
}
print('Valores sorteados: ')

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)

print('\n')
print(15 * '\033[1;31m-=-\033[m')

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
print(15 * '\033[1;31m-=-\033[m')
