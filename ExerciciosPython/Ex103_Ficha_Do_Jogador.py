"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

def ficha(gols = 0,nome = '<desconhecido>'):
    print()
    print(50*'\033[1;36m~\033[m')
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    print(50*'\033[1;36m~\033[m')


nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(gols = gols)
else:
    ficha(gols, nome)