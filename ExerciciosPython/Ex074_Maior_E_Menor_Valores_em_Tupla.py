"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
import random

numAleatorios = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100),
                 random.randint(0, 100), random.randint(0, 100))

print('Os valores sorteados foram: ', end='')
for n in numAleatorios:
    print(f'{n} ', end='')

print(f'\nO maior valor sorteado foi {max(numAleatorios)}')
print(f'O menor valor sorteado foi {min(numAleatorios)}')
