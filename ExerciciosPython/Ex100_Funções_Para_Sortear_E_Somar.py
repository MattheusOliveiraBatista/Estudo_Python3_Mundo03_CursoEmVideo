"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a
segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint
from time import sleep



def sorteia(lst):

    for i in range(0, 5):
        lst.append(randint(1, 100))

    print('Sorteando 5 valores da lista: ', end=' ')
    for k in lst:
        print(f'{k}  ', end='')
        sleep(0.4)
    print('PRONTO!')


def somaPar(Lista):
    soma = 0
    for k in Lista:
        if k % 2 == 0:
            soma += k

    print(f'Somando os valores pares da {Lista}, temos {soma}')



lista = []
sorteia(lista)
somaPar(lista)
