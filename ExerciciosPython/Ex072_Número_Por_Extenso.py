'''
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

numExtenso = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
              'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
              'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
              'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente Novamente', end='')
print(f'Você digitou o número {numExtenso[numero]}')
