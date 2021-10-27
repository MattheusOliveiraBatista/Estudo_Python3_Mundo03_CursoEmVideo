"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep


def contador(i, f, p):

    if i < f:
        print(50 * '\033[1;34m-\033[m')
        print(f'        Contagem de {i} até {f} de {p} em {p}')
        print(50 * '\033[1;34m-\033[m')
        for k in range(i, f + 1, p):
            print(f'{k}  ', end=' ', flush=True)
            sleep(0.3)
        print()
        print(50 * '\033[1;34m-\033[m')

    else:
        print()
        print(50 * '\033[1;31m-\033[m')
        print(f'        Contagem de {i} até {f} de {p} em {p}')
        print(50 * '\033[1;31m-\033[m')

        for k in range(i,f-2, -p):
            print(f'{k}  ', end= '',flush=True)
            sleep(0.3)
        print()
        print(50 * '\033[1;31m-\033[m')


contador(1, 10, 1)
contador(20, 0, 2)

print(25 * '\033[1;36m-\033[m')
print('Contador Personalizado!!')
print(25 * '\033[1;36m-\033[m')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)