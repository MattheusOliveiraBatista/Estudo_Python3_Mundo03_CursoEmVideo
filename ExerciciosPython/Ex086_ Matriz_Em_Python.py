"""
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [ [0,0,0], [0,0,0], [0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite o valor da linha [{l}, {c}]: "))

print('\n')

print(20* '-=-')
for l in range(0,3):
    for c in range(0,3):
        print(f'\033[1;32m[\033[m \033[1;40m{matriz[l][c]:^5}\033[m\033[1;32m]\033[m', end='')
    print()
print(20* '-=-')
