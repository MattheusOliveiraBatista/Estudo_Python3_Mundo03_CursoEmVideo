"""
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
"""
from Exercicio_111.utilidadesCeV import moeda

print('\033[1;31m-\033[m' * 30)
p = float(input('Digite seu preço: R$ '))
moeda.resumo(p)
