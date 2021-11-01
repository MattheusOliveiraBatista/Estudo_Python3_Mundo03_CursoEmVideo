"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de  funcionar como a função imputa(), mas com uma validação de dados para aceitar
apenas valores que seja monetários.
"""
from Exercicio_112.utilidadesCeV import dado, moeda

p = dado.leiaDinheiro('Digite um preço: ')
moeda.resumo(p, 35, 22)