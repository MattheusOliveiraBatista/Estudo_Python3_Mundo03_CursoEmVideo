"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente.
"""

numeros = list()

while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Número Duplicado, não vou adicionar...')

    op = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    if op in 'Nn':
        break

print(40*'-')
numeros.sort()
print(f'Você digitou os valores{numeros}')
print(40*'-')
