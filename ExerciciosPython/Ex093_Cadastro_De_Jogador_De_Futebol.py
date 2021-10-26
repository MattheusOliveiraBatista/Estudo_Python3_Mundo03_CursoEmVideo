"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = {'nome': str(input('Nome do Jogador:'))}

jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
jogador['total'] = 0

for c in range(0, jogador['partidas']):
    gols = (int(input(f'     Quantos gols na partida {c}?')))
    jogador['gols'].append(gols)
    jogador['total'] += gols

print(20 * '\033[1;31m-=-\033[m')
print(jogador)
print(20 * '\033[1;31m-=-\033[m')

print('\n')

print(20 * '\033[1;32m-=-\033[m')
print(f'O campo nome tem o valor {jogador["nome"]}')
print(f'O campo gols tem o valor {jogador["gols"]}')
print(f'O campo total tem o valor {jogador["total"]}')
print(20 * '\033[1;32m-=-\033[m')

print('\n')

print(20 * '\033[1;33m-=-\033[m')
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i, k in enumerate(jogador["gols"]):
    print(f'    => Na partida {i+1}, fez {k} gols.')
print(20 * '\033[1;33m-=-\033[m')
