"""Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas
que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais. """

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
