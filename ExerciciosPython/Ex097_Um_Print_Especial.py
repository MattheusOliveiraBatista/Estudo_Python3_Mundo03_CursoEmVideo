"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho adaptável.
    Ex:
        escreva(‘Olá, Mundo!’) Saída:
    ~~~~~~~~~~
    Olá, Mundo!
    ~~~~~~~~~~
"""

def escreve(msg):
    print(len(msg)*'\033[1;34m-\033[m')
    print(msg)
    print(len(msg)*'\033[1;34m-\033[m')



escreve('Ola Mundo')
escreve('Matheus Batista de Oliveira')