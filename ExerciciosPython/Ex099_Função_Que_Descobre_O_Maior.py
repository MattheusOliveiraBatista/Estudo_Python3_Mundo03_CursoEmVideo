"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def maior(a, b):
    print()
    print(f'O valor recebido para A foi {a}.')
    print(f'O valor recebido para B foi {b}.')

    menor = 0
    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a

    print()
    print(25 * '\033[1;31m-\033[m')
    print(f'  O maior valor foi {maior}.  \n  O menor valor foi {menor}.')
    print(25 * '\033[1;31m-\033[m')


print(25 * '\033[1;36m-\033[m')
print(' Qual número é maior?     ')
num1 = int(input('Digite o Primeiro Termo:'))
num2 = int(input('Digite o Segundo Termo:'))
print(25 * '\033[1;36m-\033[m')
maior(num1, num2)
