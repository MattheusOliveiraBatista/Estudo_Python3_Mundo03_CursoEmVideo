"""
Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.
"""


def soma(a, b):
    print(20 * '-=-')
    print(f'\033[1;36m FUNÇÃO PARA SOMAR COM OS PARÂMETROS:\033[m \033[1;33ma = {a} && b = {b}\033[m')
    print(f'  RESULTADO DA SOMA:      {a} + {b} = {a + b}')
    print(20 * '-=-')
    print()


# Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)


# * é o símbolo de desempacotar
# podemos passar N parâmetros
# O retorno será uma Tupla
def contador(*num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

print('\n\n')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
