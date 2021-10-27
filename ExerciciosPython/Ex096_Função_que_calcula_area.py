"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""


def terreno(larg, alt):
    print(30 * '\033[1;39m-\033[m')
    print(f'Largura: {larg} || Altura: {alt}')
    print(f'Área total do terreno: {larg*alt} m²')
    print(30 * '\033[1;39m-\033[m')


print(30 * '\033[1;34m-\033[m')
print('\033[1;39m   CONTROLE DE TERRENOS\033[m')
print(30 * '\033[1;34m-\033[m')

largura = float(input('Largura (m): '))
altura = float(input('Altura (m): '))

terreno(largura,altura)
