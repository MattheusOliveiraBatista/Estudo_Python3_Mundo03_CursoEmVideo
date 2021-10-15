"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
valores = []
maior = menor = 0

print(35* '\033[1;32m=\033[m')

for c in range(0,5):
    valores.append(int(input(f'Digite um valor na posição [{c}]: ')))
    if c == 0:
        maior = menor = valores[0]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(35* '\033[1;32m=\033[m')


print(25* '\033[1;40m=\033[m')
print(f'Maior: {maior} || Menor: {menor}')
print(25* '\033[1;40m=\033[m')

