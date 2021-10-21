"""
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves
"""
pessoa = []
cadastro = []
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        maior = menor = pessoa[1]

    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        elif pessoa[1] < menor:
            menor = pessoa[1]
    cadastro.append(pessoa[:])
    pessoa.clear()
    op = str(input('Deseja Continuar? [S/N]')).strip()[0]
    if op in 'Nn':
        break

print(30*'\033[1;32m=\033[m')
print(f'Os dados foram {cadastro}')
print(f'Ao todo, você cadastrou {len(cadastro)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de', end='')
for p in cadastro:
    if p[1] == maior:
        print(f' [{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de', end='')
for p in cadastro:
    if p[1] == menor:
        print(f' [{p[0]}]', end='')
print()
print(30*'\033[1;32m=\033[m')
