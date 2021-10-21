"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. """
numeros = [[], []]
valor = 0

for i in range(1, 8):
    valor = int(input(f'Digite o {i}° valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print('\n')
print(50*'\033[1;31m=\033[m')
print(f'Todos os valores: {numeros}')
print(f'Valores Pares na ordem natural na Lista: {numeros[0]}')
print(f'Valores ímpares na ordem natural na Lista: {numeros[1]}')

numeros[0].sort()
numeros[1].sort()

print(f'Valores Pares na ordem crescente na Lista: {numeros[0]}')
print(f'Valores ímpares na ordem crescente na Lista: {numeros[1]}')
print(50*'\033[1;31m=\033[m')
