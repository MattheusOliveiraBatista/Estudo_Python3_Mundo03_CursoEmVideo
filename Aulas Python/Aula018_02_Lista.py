"""Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas
que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais. """

galera = list()
dado = []
maior = menor = 0

for c in range(0, 3):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digite sua idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade!')
        menor += 1

print(f'Temos {maior} maiores e {menor} menores de idade.')
