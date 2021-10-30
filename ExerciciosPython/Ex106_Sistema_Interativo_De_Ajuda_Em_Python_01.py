"""
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai
digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra
'FIM', o programa se encerrará. Importante: use cores.
"""

def ajuda(com):
    help(com)


def titulo(msg):  # cor=0):
    tam = len(msg) + 4
    print('\033[1;36m~\033[m' * tam)
    print(f' {msg}')
    print('\033[1;36m~\033[m' * tam)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input("Função ou Biblioteca > "))

    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
