"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 

A) A soma de todos os valores pares digitados. 
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.
"""

matriz = [ [0,0,0], [0,0,0], [0,0,0]]
valorPar = 0
valorImpar = 0
TerceiraColuna = 0
valorSegundaLinha = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite o valor da linha [{l}, {c}]: "))
        if matriz[l][c] % 2 == 0: 
            valorPar += matriz[l][c]
        else:
            valorImpar += matriz[l][c]

        if matriz[l][2]:
            TerceiraColuna += matriz[l][2]

        if matriz[1][c] > valorSegundaLinha:
            valorSegundaLinha = matriz[1][c]

print('\n')

print(20* '-=-')
for l in range(0,3):
    for c in range(0,3):
        print(f'\033[1;32m[\033[m \033[1;40m{matriz[l][c]:^5}\033[m\033[1;32m]\033[m', end='')
    print()
print(20* '-=-')
print(f'A soma dos valores ímpares é {valorImpar}.')
print(f'A soma dos valores pares é {valorPar}.')
print(f'A soma dos valores da terceira coluna é {TerceiraColuna}.')
print(f'O maior valor da segunda linha é {valorSegundaLinha}.')
print(20* '-=-')