"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter 
apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

lista = []
listaImpar = []
listaPar = []

while True:
    lista.append(int(input('Digite um valor: ')))

    op = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    if op in 'Nn':
        break

for c in lista:
    if c % 2 == 0:
        listaPar.append(c)
    else:
        listaImpar.append(c)

print(30*'=')
print(f'A lista completa é {lista}')
print(f'A lista completa de Pares é {listaPar}')
print(f'A lista completa de Ímpares é {listaImpar}')
print(40*'=')
