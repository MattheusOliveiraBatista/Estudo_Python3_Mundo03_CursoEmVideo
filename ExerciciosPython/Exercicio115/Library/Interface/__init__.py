"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e  idade em um arquivo de texto simples.

O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

Vamos criar um menu em Python, usando modularização.
"""
def leiaInt(msg):
    while True:
        try:
            n = int(input(f'\033[1;36m{msg}\033[m'))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '\033[1;31m-\033[m' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;36m{c}\033[m - \033[1;32m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
